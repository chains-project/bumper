```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingRequest;

public class AbstractThemeMojo {
    public void execute() {
        MavenSession session = new MavenSession();
        ProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
        ProjectBuilder builder = session.getProjectBuilder();
        builder.build(buildingRequest, new MavenProject());
    }
}
```