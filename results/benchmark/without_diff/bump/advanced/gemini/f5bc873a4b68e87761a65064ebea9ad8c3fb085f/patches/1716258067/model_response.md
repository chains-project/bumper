```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuildingRequest;
import org.eclipse.aether.RepositorySystem;
import org.eclipse.aether.RepositorySystemSession;
import org.eclipse.aether.artifact.Artifact;
import org.eclipse.aether.artifact.DefaultArtifact;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactRequest;
import org.eclipse.aether.resolution.ArtifactResolutionException;
import org.eclipse.aether.resolution.ArtifactResult;

import java.util.Collections;
import java.util.List;

public abstract class AbstractThemeMojo extends AbstractMojo {

    /**
     * @parameter expression="${project}"
     * @required
     * @readonly
     */
    protected MavenProject project;

    /**
     * @component
     * @required
     * @readonly
     */
    protected RepositorySystem repoSystem;

    /**
     * @parameter default-value="${repositorySystemSession}"
     * @required
     * @readonly
     */
    protected RepositorySystemSession repoSession;

    /**
     * @parameter default-value="${remoteRepositories}"
     * @required
     * @readonly
     */
    protected List<RemoteRepository> remoteRepos;

    /**
     * @component
     */
    protected MavenSession session;

    /**
     * The artifact to build.
     *
     * @parameter
     * @required
     */
    protected Artifact artifact;

    /**
     * The artifact to build.
     *
     * @parameter
     */
    protected String artifactVersion;

    /**
     * The artifact to build.
     *
     * @parameter
     */
    protected String artifactClassifier;

    protected Artifact getResolvedArtifact() throws ArtifactResolutionException {
        // get the artifact to build
        if (artifactVersion == null) {
            artifactVersion = project.getVersion();
        }
        if (artifactClassifier == null) {
            artifactClassifier = "";
        }
        artifact = new DefaultArtifact(artifact.getGroupId(), artifact.getArtifactId(), artifactClassifier, artifact.getExtension(), artifactVersion);

        // resolve the artifact
        ArtifactRequest artifactRequest = new ArtifactRequest();
        artifactRequest.setArtifact(artifact);
        artifactRequest.setRepositories(remoteRepos);

        ArtifactResult artifactResult = repoSystem.resolveArtifact(repoSession, artifactRequest);
        return artifactResult.getArtifact();
    }

    protected MavenProject getResolvedProject() throws ArtifactResolutionException {
        Artifact resolvedArtifact = getResolvedArtifact();

        ProjectBuildingRequest request = new ProjectBuildingRequest();
        request.setLocalRepository(session.getLocalRepository());
        request.setRemoteRepositories(remoteRepos);
        request.setProject(project);

        return session.getProjectBuilder().build(resolvedArtifact, request).getProject();
    }
}
```