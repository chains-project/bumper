Here's the patched version of the failing method:
```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingException;
import org.apache.maven.execution.MavenSession;
import org.eclipse.aether.DefaultRepositorySystemSession;

// ...

private MavenProject getProject(String groupId, String artifactId, String version) {
    DefaultRepositorySystemSession repositorySystemSession = (DefaultRepositorySystemSession) session.getRepositorySession();
    ProjectBuilder projectBuilder = repositorySystemSession.getProjectBuilder();

    try {
        return projectBuilder.buildProject(
            new File(session.getCurrentProject().getBasedir(), String.format("%s-%s.pom", artifactId, version)),
            session.getRepositorySession()
        );
    } catch (ProjectBuildingException e) {
        throw new MojoFailureException("Failed to build project", e);
    }
}
```
In the new library version, the `MavenProject` is now constructed using `ProjectBuilder`. I have updated the code to use the new method of constructing `MavenProject`.