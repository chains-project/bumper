```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingRequest;

public abstract class AbstractThemeMojo extends AbstractMojo {

  @Parameter(defaultValue = "${session}", readonly = true)
  private MavenSession session;

  @Parameter(defaultValue = "${project}", readonly = true)
  private MavenProject project;

  @Component
  private ProjectBuilder projectBuilder;

  protected MavenProject getMavenProject() {
    ProjectBuildingRequest request = new ProjectBuildingRequest();
    request.setSession(session);
    request.setProject(project);
    return projectBuilder.build(request).getProject();
  }
}
```