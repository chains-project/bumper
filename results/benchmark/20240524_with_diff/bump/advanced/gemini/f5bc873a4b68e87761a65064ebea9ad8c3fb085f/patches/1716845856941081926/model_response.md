```java
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.logging.Log;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.util.DirectoryScanner;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public abstract class AbstractThemeMojo extends AbstractMojo {

  /**
   * The source directory containing the theme files.
   *
   * @parameter default-value="${project.basedir}/src/main/webapp/tobago"
   */
  private File sourceDirectory;

  /**
   * The output directory where the theme files will be copied.
   *
   * @parameter default-value="${project.build.directory}/classes"
   */
  private File outputDirectory;

  /**
   * The list of files to include. Specified as fileset patterns which are relative to the source directory.
   *
   * @parameter
   */
  private List<String> includes;

  /**
   * The list of files to exclude. Specified as fileset patterns which are relative to the source directory.
   *
   * @parameter
   */
  private List<String> excludes;

  /**
   * Whether to include the default files.
   *
   * @parameter default-value="true"
   */
  private boolean includeDefault;

  /**
   * The project instance.
   *
   * @parameter expression="${project}"
   * @required
   * @readonly
   */
  private MavenProject project;

  /**
   * The logger.
   *
   * @parameter default-value="${logger}"
   * @required
   * @readonly
   */
  private Log log;

  /**
   * Execute the mojo.
   *
   * @throws MojoExecutionException if an error occurs.
   */
  @Override
  public void execute() throws MojoExecutionException {
    if (includes == null || includes.isEmpty()) {
      includes = new ArrayList<>();
      includes.add("**/*");
    }
    if (excludes == null) {
      excludes = new ArrayList<>();
    }
    if (includeDefault) {
      includes.addAll(getDefaultIncludes());
    }
    // exclude all files in the default directory
    excludes.add(getDefaultDirectory() + "/**/*");
    // exclude all files in the target directory
    excludes.add(getTargetDirectory() + "/**/*");

    final DirectoryScanner scanner = new DirectoryScanner();
    scanner.setBasedir(sourceDirectory);
    scanner.setIncludes(includes.toArray(new String[0]));
    scanner.setExcludes(excludes.toArray(new String[0]));
    scanner.scan();
    final String[] files = scanner.getIncludedFiles();
    for (final String file : files) {
      final File sourceFile = new File(sourceDirectory, file);
      final File targetFile = new File(outputDirectory, file);
      if (!targetFile.getParentFile().exists()) {
        if (!targetFile.getParentFile().mkdirs()) {
          throw new MojoExecutionException("Failed to create directory: " + targetFile.getParentFile());
        }
      }
      try {
        copyFile(sourceFile, targetFile);
      } catch (IOException e) {
        throw new MojoExecutionException("Failed to copy file: " + sourceFile, e);
      }
    }
  }

  /**
   * Get the default includes.
   *
   * @return the default includes.
   */
  protected abstract List<String> getDefaultIncludes();

  /**
   * Get the default directory.
   *
   * @return the default directory.
   */
  protected abstract String getDefaultDirectory();

  /**
   * Get the target directory.
   *
   * @return the target directory.
   */
  protected abstract String getTargetDirectory();

  /**
   * Copy a file.
   *
   * @param sourceFile the source file.
   * @param targetFile the target file.
   * @throws IOException if an error occurs.
   */
  private void copyFile(final File sourceFile, final File targetFile) throws IOException {
    if (sourceFile.isDirectory()) {
      targetFile.mkdirs();
    } else {
      if (sourceFile.lastModified() > targetFile.lastModified()) {
        log.info("Copying " + sourceFile + " to " + targetFile);
        project.getBuild().addResource(sourceFile.getPath(), targetFile.getParentFile().getPath());
      }
    }
  }
}
```