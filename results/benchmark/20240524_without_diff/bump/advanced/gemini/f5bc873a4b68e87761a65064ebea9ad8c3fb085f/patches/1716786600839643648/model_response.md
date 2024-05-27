```java
import org.eclipse.aether.artifact.Artifact;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactRequest;
import org.eclipse.aether.resolution.ArtifactResolutionException;
import org.eclipse.aether.resolution.ArtifactResult;
import org.eclipse.aether.resolution.VersionRangeRequest;
import org.eclipse.aether.resolution.VersionRangeResolutionException;
import org.eclipse.aether.resolution.VersionRangeResult;
import org.eclipse.aether.util.artifact.DefaultArtifact;
import org.eclipse.aether.util.version.GenericVersionScheme;

import java.util.List;
import java.util.Objects;

/**
 * This class provides methods to resolve artifacts from a remote repository.
 */
public class ArtifactResolver {

  private final MavenProject mavenProject;
  private final List<RemoteRepository> remoteRepositories;

  /**
   * Constructor.
   *
   * @param mavenProject the Maven project
   * @param remoteRepositories the remote repositories
   */
  public ArtifactResolver(MavenProject mavenProject, List<RemoteRepository> remoteRepositories) {
    this.mavenProject = mavenProject;
    this.remoteRepositories = remoteRepositories;
  }

  /**
   * Resolves an artifact from a remote repository.
   *
   * @param artifactId the artifact ID
   * @param groupId the group ID
   * @param versionRange the version range
   * @return the resolved artifact
   * @throws ArtifactResolutionException if the artifact could not be resolved
   */
  public Artifact resolveArtifact(String artifactId, String groupId, String versionRange)
      throws ArtifactResolutionException {
    Artifact artifact = new DefaultArtifact(groupId, artifactId, "", "jar", versionRange);
    ArtifactRequest artifactRequest = new ArtifactRequest();
    artifactRequest.setArtifact(artifact);
    artifactRequest.setRepositories(remoteRepositories);

    ArtifactResult artifactResult = mavenProject.getProjectBuilder().build(artifactRequest);

    if (artifactResult.isMissing()) {
      throw new ArtifactResolutionException("Artifact not found: " + artifact);
    }

    return artifactResult.getArtifact();
  }

  /**
   * Resolves the latest version of an artifact from a remote repository.
   *
   * @param artifactId the artifact ID
   * @param groupId the group ID
   * @return the latest version of the artifact
   * @throws VersionRangeResolutionException if the latest version could not be resolved
   */
  public String resolveLatestVersion(String artifactId, String groupId)
      throws VersionRangeResolutionException {
    Artifact artifact = new DefaultArtifact(groupId, artifactId, "", "jar", "[0,)");
    VersionRangeRequest versionRangeRequest = new VersionRangeRequest();
    versionRangeRequest.setArtifact(artifact);
    versionRangeRequest.setRepositories(remoteRepositories);

    VersionRangeResult versionRangeResult = mavenProject.getProjectBuilder().build(versionRangeRequest);

    List<String> versions = versionRangeResult.getVersions();
    if (versions.isEmpty()) {
      throw new VersionRangeResolutionException("No versions found for artifact: " + artifact);
    }

    // Sort versions in descending order
    versions.sort(new GenericVersionScheme().new Comparator());

    // Return the latest version
    return versions.get(0);
  }

  /**
   * Checks if an artifact exists in a remote repository.
   *
   * @param artifactId the artifact ID
   * @param groupId the group ID
   * @param version the version
   * @return true if the artifact exists, false otherwise
   * @throws ArtifactResolutionException if the artifact could not be checked
   */
  public boolean artifactExists(String artifactId, String groupId, String version)
      throws ArtifactResolutionException {
    Artifact artifact = new DefaultArtifact(groupId, artifactId, "", "jar", version);
    ArtifactRequest artifactRequest = new ArtifactRequest();
    artifactRequest.setArtifact(artifact);
    artifactRequest.setRepositories(remoteRepositories);

    ArtifactResult artifactResult = mavenProject.getProjectBuilder().build(artifactRequest);

    return !artifactResult.isMissing();
  }

  /**
   * Checks if two artifacts are equal.
   *
   * @param artifact1 the first artifact
   * @param artifact2 the second artifact
   * @return true if the artifacts are equal, false otherwise
   */
  public static boolean artifactsEqual(Artifact artifact1, Artifact artifact2) {
    return Objects.equals(artifact1.getGroupId(), artifact2.getGroupId())
        && Objects.equals(artifact1.getArtifactId(), artifact2.getArtifactId())
        && Objects.equals(artifact1.getVersion(), artifact2.getVersion())
        && Objects.equals(artifact1.getClassifier(), artifact2.getClassifier())
        && Objects.equals(artifact1.getExtension(), artifact2.getExtension());
  }
}
```