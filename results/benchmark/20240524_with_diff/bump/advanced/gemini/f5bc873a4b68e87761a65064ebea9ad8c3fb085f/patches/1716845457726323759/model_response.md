```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuildingRequest;

public abstract class AbstractThemeMojo extends AbstractMojo {

  @Parameter(defaultValue = "${session}", readonly = true)
  private MavenSession session;

  @Override
  protected void execute() throws Exception {
    ProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
    buildingRequest.setRepositorySession(session.getRepositorySession());
    buildingRequest.setProject(getProject());
    MavenProject project = session.getProjectBuildingRequest().build(project);
    // ...
  }

  protected MavenProject getProject() {
    return session.getCurrentProject();
  }
}
```