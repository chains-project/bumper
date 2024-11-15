```java
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.util.DirectoryScanner;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * This goal copies the theme resources from the source directory to the destination directory.
 *
 * @since 4.0.0
 */
@Mojo(name = "copy-theme-resources")
public class CopyThemeResourcesMojo extends AbstractThemeMojo {

  @Parameter(defaultValue = "${project}", readonly = true)
  private MavenProject project;

  @Parameter(property = "sourceDirectory", required = true)
  private File sourceDirectory;

  @Parameter(property = "destinationDirectory", required = true)
  private File destinationDirectory;

  @Parameter(property = "includes", required = true)
  private String[] includes;

  @Parameter(property = "excludes", required = true)
  private String[] excludes;

  @Override
  public void execute() throws MojoExecutionException, MojoFailureException {
    try {
      final List<String> filesToCopy = new ArrayList<>();
      final DirectoryScanner scanner = new DirectoryScanner();
      scanner.setBasedir(sourceDirectory);
      scanner.setIncludes(includes);
      scanner.setExcludes(excludes);
      scanner.scan();
      for (final String file : scanner.getIncludedFiles()) {
        filesToCopy.add(file);
      }
      copyFiles(filesToCopy, sourceDirectory, destinationDirectory);
    } catch (IOException e) {
      throw new MojoExecutionException("Error copying theme resources", e);
    }
  }

  private void copyFiles(final List<String> filesToCopy, final File sourceDirectory, final File destinationDirectory)
      throws IOException {
    for (final String file : filesToCopy) {
      final File sourceFile = new File(sourceDirectory, file);
      final File destinationFile = new File(destinationDirectory, file);
      if (!destinationFile.getParentFile().mkdirs()) {
        throw new IOException("Failed to create directory: " + destinationFile.getParentFile());
      }
      if (!sourceFile.renameTo(destinationFile)) {
        throw new IOException("Failed to copy file: " + sourceFile);
      }
    }
  }
}
```