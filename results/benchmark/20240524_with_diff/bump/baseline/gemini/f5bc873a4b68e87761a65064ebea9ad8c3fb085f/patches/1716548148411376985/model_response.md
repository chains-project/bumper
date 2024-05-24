```java
import org.apache.maven.artifact.resolver.ArtifactResolutionException;

  public void execute() throws MojoExecutionException {
    try {
      MojoHelper.setupLogging(getLog());

      // ...

      final Set<Artifact> artifacts = artifactManager.resolveArtifacts(
          session,
          project.getArtifacts(),
          remoteRepositories,
          artifactFilter,
          getLocalRepository());

      // ...

    } catch (ArtifactResolutionException e) {
      throw new MojoExecutionException(e.getMessage(), e);
    }
  }
```