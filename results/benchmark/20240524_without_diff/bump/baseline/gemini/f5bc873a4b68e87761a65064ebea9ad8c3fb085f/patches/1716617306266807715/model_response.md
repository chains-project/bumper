```java
import org.apache.maven.artifact.DependencyResolutionRequiredException;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;
import org.apache.myfaces.tobago.maven.plugin.AbstractUnpackMojo;
import org.apache.myfaces.tobago.maven.plugin.util.Theme;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/**
 * Unpacks a theme from a WAR file.
 *
 * @since 5.0.0
 */
@Mojo(name = "unpack-theme", requiresDependencyResolution = ResolutionScope.NONE)
public class UnPackThemeMojo extends AbstractUnpackMojo {

  /**
   * The theme to unpack.
   */
  @Parameter(property = "theme", required = true)
  private String theme;

  /**
   * The version of the theme to unpack.
   */
  @Parameter(property = "themeVersion", defaultValue = "1.0.0")
  private String themeVersion;

  /**
   * The base directory of the theme.
   */
  @Parameter(property = "themeBaseDir", defaultValue = "${project.basedir}/src/main/webapp/WEB-INF/tobago/theme")
  private File themeBaseDir;

  /**
   * The directory to unpack the theme to.
   */
  @Parameter(property = "unpackDir", defaultValue = "${project.build.directory}/tobago/theme")
  private File unpackDir;

  /**
   * The list of files to copy from the theme.
   */
  @Parameter(property = "files")
  private List<String> files;

  @Override
  public void execute() throws MojoExecutionException {

    final MavenProject project = getProject();
    final Theme theme = new Theme(project, this.theme, this.themeVersion);

    try {
      final Path unpackDir = unpackDir.toPath();
      Files.createDirectories(unpackDir);

      final Path themeDir = theme.getThemeDir().toPath();
      if (files == null || files.isEmpty()) {
        copyAll(themeDir, unpackDir);
      } else {
        for (final String file : files) {
          final Path source = themeDir.resolve(file);
          final Path target = unpackDir.resolve(file);
          Files.copy(source, target);
        }
      }

    } catch (final IOException e) {
      throw new MojoExecutionException("Failed to unpack theme '" + this.theme + "'.", e);
    } catch (final DependencyResolutionRequiredException e) {
      throw new MojoExecutionException("Failed to resolve theme '" + this.theme + "'.", e);
    }
  }
}
```