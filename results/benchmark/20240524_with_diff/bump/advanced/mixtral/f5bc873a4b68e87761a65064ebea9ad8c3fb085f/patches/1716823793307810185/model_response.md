Here is a proposed patch for the client code:
```java
import org.apache.maven.model.Model;
import org.apache.maven.project.MavenProject;
import org.eclipse.aether.RepositorySystem;
import org.eclipse.aether.RepositorySystemSession;
import org.eclipse.aether.collection.CollectRequest;
import org.eclipse.aether.collection.CollectResult;
import org.eclipse.aether.connector.basic.BasicRepositoryConnectorFactory;
import org.eclipse.aether.impl.DefaultServiceLocator;
import org.eclipse.aether.repository.LocalRepository;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactRequest;
import org.eclipse.aether.resolution.ArtifactResolutionException;
import org.eclipse.aether.resolution.ArtifactResult;
import org.eclipse.aether.spi.connector.RepositoryConnectorFactory;
import org.eclipse.aether.spi.locator.ServiceLocator;
import org.eclipse.aether.transfer.TransferCancelledException;
import org.eclipse.aether.transfer.TransferFailedException;

// ...

private RepositorySystem repoSystem;
private RepositorySystemSession repoSession;
private LocalRepository localRepo;
private RemoteRepository remoteRepo;

public void execute() throws MojoExecutionException {
    // ...

    DefaultServiceLocator locator = MavenUtil.serviceLocator();
    locator.addService(RepositoryConnectorFactory.class, BasicRepositoryConnectorFactory.class);
    repoSystem = locator.getService(RepositorySystem.class);

    repoSession = repoSystem.newSession();
    localRepo = new LocalRepository(getLocalRepositoryPath());
    remoteRepo = new RemoteRepository.Builder("central", "default", "https://repo.maven.apache.org/maven2/").build();
    repoSession.setLocalRepositoryManager(repoSystem.newLocalRepositoryManager(localRepo));

    // ...
}

private Model getModel(String groupId, String artifactId, String version) throws MojoExecutionException {
    try {
        ArtifactRequest artifactRequest = new ArtifactRequest();
        artifactRequest.setArtifact(new DefaultArtifact(groupId, artifactId, version, "pom"));
        artifactRequest.setRepositories(Arrays.asList(remoteRepo));
        ArtifactResult artifactResult = repoSystem.resolveArtifact(repoSession, artifactRequest);
        return repoSystem.readModel(repoSession, artifactResult.getArtifact().getFile());
    } catch (ArtifactResolutionException | TransferFailedException | TransferCancelledException e) {
        throw new MojoExecutionException("Failed to resolve artifact", e);
    }
}
```
The changes include importing the necessary classes for working with Aether to resolve dependencies and downloading the POM file. The `execute()` method creates a `RepositorySystem` instance and sets up the local and remote repositories. The `getModel()` method uses the `RepositorySystem` to resolve the POM file for the given artifact.