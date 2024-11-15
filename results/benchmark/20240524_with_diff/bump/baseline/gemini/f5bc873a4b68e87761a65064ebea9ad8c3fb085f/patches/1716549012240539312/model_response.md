```java
import org.apache.maven.plugin.MojoExecutionException;

  /**
   * Unpacks a theme into the target directory.
   */
public class UnPackThemeMojo extends AbstractThemeMojo {

  /**
   * @param session
   * @throws MojoExecutionException
   */
  @Override
  protected void execute(MavenSession session) throws MojoExecutionException {
    try {
      final UnPackThemeRequest request = new UnPackThemeRequest(session, project, projectHelper,
          theme, themeVersion, targetDirectory, artifactHandler, artifactHandlerMapping,
          fileSystem, fileManager, resourceUtil, log);
      new UnPackTheme().execute(request);
    } catch (IOException e) {
      throw new MojoExecutionException("Error unpacking theme", e);
    }
  }
}
```