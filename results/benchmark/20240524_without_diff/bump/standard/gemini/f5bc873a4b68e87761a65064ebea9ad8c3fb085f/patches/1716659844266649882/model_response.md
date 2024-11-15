```java
import org.eclipse.aether.artifact.Artifact;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactRequest;
import org.eclipse.aether.resolution.ArtifactResolutionException;
import org.eclipse.aether.resolution.ArtifactResult;

import java.io.File;
import java.util.List;

/**
 * Created by alexandros on 2021-08-20.
 */
public abstract class AbstractThemeMojo extends AbstractMojo {

  /**
   * @parameter default-value="${project}"
   * @required
   * @readonly
   */
  protected MavenProject project;

  /**
   * @parameter default-value="${localRepository}"
   * @required
   * @readonly
   */
  protected Repository localRepository;

  /**
   * @parameter default-value="${remoteRepositories}"
   * @required
   * @readonly
   */
  protected List<RemoteRepository> remoteRepositories;

  protected File resolveArtifact(final Artifact artifact) throws ArtifactResolutionException {
    final ArtifactRequest artifactRequest = new ArtifactRequest();
    artifactRequest.setArtifact(artifact);
    artifactRequest.setRepositories(remoteRepositories);

    final ArtifactResult artifactResult = repositorySystem.resolveArtifact(repositorySession, artifactRequest);
    return artifactResult.getArtifact().getFile();
  }
}
```