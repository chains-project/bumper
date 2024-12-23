```java
import org.codehaus.plexus.util.DirectoryScanner;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

/**
 * Goal which copies the web-resources.
 *
 * @since 3.0.0
 */
@Mojo(name = "copy-web-resources")
public class CopyWebResourcesMojo extends AbstractThemeMojo {

  @Parameter(defaultValue = "${project}", readonly = true)
  private MavenProject project;

  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-plugin/web-resources", required = true)
  private File outputDirectory;

  @Parameter(required = true)
  private List<Resource> resources = new ArrayList<>();

  @Override
  public void execute() throws MojoExecutionException {
    getLog().info("Copying web-resources");
    if (outputDirectory.exists()) {
      outputDirectory.delete();
    }
    outputDirectory.mkdirs();
    for (Resource resource : resources) {
      DirectoryScanner scanner = new DirectoryScanner();
      scanner.setBasedir(resource.getSourceDirectory());
      scanner.setIncludes(resource.getIncludes());
      scanner.setExcludes(resource.getExcludes());
      scanner.scan();
      String[] files = scanner.getIncludedFiles();
      for (String file : files) {
        File source = new File(resource.getSourceDirectory(), file);
        File target = new File(outputDirectory, file);
        if (target.getParentFile() != null) {
          target.getParentFile().mkdirs();
        }
        try {
          copyFile(source, target);
        } catch (Exception e) {
          throw new MojoExecutionException("Error copying file " + source + " to " + target, e);
        }
      }
    }
  }
}
```