```java
  import org.apache.maven.artifact.DependencyResolutionRequiredException;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;

/**
 * Unpack a Tobago theme.
 */
@Mojo(name = "unpack-theme")
public class UnPackThemeMojo extends AbstractThemeMojo {

  /**
   * The theme to unpack.
   */
  @Parameter(property = "theme", required = true)
  private String theme;

  /**
   * The directory to unpack the theme to.
   */
  @Parameter(property = "targetDirectory", required = true)
  private File targetDirectory;

  @Override
  public void execute() throws MojoExecutionException, MojoFailureException {
    try {
      final File themeFile = getThemeFile(theme);
      if (themeFile.exists()) {
        final File themeDirectory = new File(targetDirectory, theme);
        themeDirectory.mkdirs();

        // Unpack the theme
        final ZipFile zipFile = new ZipFile(themeFile);
        final Enumeration<? extends ZipEntry> entries = zipFile.entries();
        while (entries.hasMoreElements()) {
          final ZipEntry entry = entries.nextElement();
          final File file = new File(themeDirectory, entry.getName());
          if (!entry.isDirectory()) {
            final InputStream inputStream = zipFile.getInputStream(entry);
            final FileOutputStream outputStream = new FileOutputStream(file);
            IOUtils.copy(inputStream, outputStream);
            inputStream.close();
            outputStream.close();
          } else {
            file.mkdirs();
          }
        }
        zipFile.close();
      } else {
        throw new MojoFailureException("Theme '" + theme + "' not found.");
      }
    } catch (final IOException e) {
      throw new MojoExecutionException("Error unpacking theme '" + theme + "': " + e.getMessage(), e);
    }
  }
}
```