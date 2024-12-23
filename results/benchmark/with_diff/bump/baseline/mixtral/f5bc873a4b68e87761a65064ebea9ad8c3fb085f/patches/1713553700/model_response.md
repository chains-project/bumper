Here's the fixed `unpackTheme` method with the required import statement. I added a try-with-resources statement to handle the `ArtifactResolver` and changed the exception to `ArtifactResolutionException`.

```java
import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.ArtifactRequest;
import org.apache.maven.artifact.ArtifactResolver;
import org.apache.maven.artifact.repository.ArtifactRepository;
import org.apache.maven.artifact.resolver.ArtifactResolutionException;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.components.interactivity.Prompter;

import java.io.File;
import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

public class UnPackThemeMojo extends AbstractMojo {

    // ...

    @Override
    public void execute() throws MojoExecutionException {
        // ...

        ArtifactResolver artifactResolver = (ArtifactResolver) getPluginContext().get(ResolutionUtils.ARTIFACT_RESOLVER);
        ArtifactRepository localRepository = (ArtifactRepository) getPluginContext().get(ResolutionUtils.LOCAL_REPOSITORY);

        try (ArtifactResolver finalArtifactResolver = artifactResolver) {
            // ...

            List<Artifact> artifacts = getArtifacts();

            for (Artifact artifact : artifacts) {
                ArtifactRequest request = new ArtifactRequest();
                request.setArtifact(artifact);
                request.setRepositories(List.of(localRepository));

                Artifact resolvedArtifact = null;

                try {
                    resolvedArtifact = finalArtifactResolver.resolveArtifact(request);
                } catch (ArtifactResolutionException e) {
                    throw new MojoExecutionException("Failed to resolve artifact: " + artifact, e);
                }

                // ...
            }
        } catch (IOException e) {
            throw new MojoExecutionException("Failed to close ArtifactResolver", e);
        }
    }

    // ...
}
```