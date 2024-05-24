```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingRequest;

public class AbstractThemeMojo {
    public void execute() {
        ProjectBuildingRequest buildingRequest = new DefaultProjectBuildingRequest();
        MavenSession session = new MavenSession();
        buildingRequest.setProcessPlugins(false);
        ProjectBuilder projectBuilder = session.getProjectBuilder();
        MavenProject project = projectBuilder.build(buildingRequest).getProject();
        // rest of the code
    }
}
```