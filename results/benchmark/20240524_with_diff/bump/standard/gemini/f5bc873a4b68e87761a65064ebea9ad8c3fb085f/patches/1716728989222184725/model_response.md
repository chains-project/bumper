```java
import org.eclipse.aether.artifact.Artifact;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactRequest;
import org.eclipse.aether.resolution.ArtifactResolutionException;
import org.eclipse.aether.resolution.ArtifactResult;
import org.eclipse.aether.util.artifact.DefaultArtifact;

import java.io.File;
import java.util.List;

/**
 * @since 1.0.0
 */
public abstract class AbstractThemeMojo extends AbstractMojo {

  /**
   * @since 1.0.0
   */
  protected abstract List<Artifact> getThemeArtifacts();

  /**
   * @since 1.0.0
   */
  protected abstract List<RemoteRepository> getThemeRepositories();

  /**
   * @since 1.0.0
   */
  protected abstract File getThemeOutputDirectory();

  /**
   * @since 1.0.0
   */
  protected abstract File getThemeSourceDirectory();

  /**
   * @since 1.0.0
   */
  protected abstract String getThemeVersion();

  /**
   * @since 1.0.0
   */
  protected abstract void processTheme(final File themeDirectory);

  @Override
  public void execute() throws MojoExecutionException {
    final List<Artifact> themeArtifacts = getThemeArtifacts();
    final List<RemoteRepository> themeRepositories = getThemeRepositories();
    final File themeOutputDirectory = getThemeOutputDirectory();
    final File themeSourceDirectory = getThemeSourceDirectory();
    final String themeVersion = getThemeVersion();

    try {
      final ArtifactRequest artifactRequest = new ArtifactRequest();
      artifactRequest.setArtifacts(themeArtifacts);
      artifactRequest.setRepositories(themeRepositories);

      final ArtifactResult artifactResult = session.getSystemSession().getArtifactResolver().resolveArtifacts(session.getRepositorySession(), artifactRequest);

      for (final Artifact artifact : artifactResult.getArtifacts()) {
        final File artifactFile = artifact.getFile();
        final File themeDirectory = new File(themeOutputDirectory, artifact.getArtifactId() + "-" + themeVersion);
        FileUtils.copyDirectory(artifactFile, themeDirectory);
        processTheme(themeDirectory);
      }

      final File themeDirectory = new File(themeOutputDirectory, "tobago-theme-" + themeVersion);
      FileUtils.copyDirectory(themeSourceDirectory, themeDirectory);
      processTheme(themeDirectory);

    } catch (final ArtifactResolutionException e) {
      throw new MojoExecutionException("Failed to resolve theme artifacts.", e);
    } catch (final IOException e) {
      throw new MojoExecutionException("Failed to copy theme artifacts.", e);
    }
  }
}
```