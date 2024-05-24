```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuildingRequest;

public class AbstractThemeMojo {
    public void execute() {
        MavenSession session = new MavenSession();
        ProjectBuildingRequest buildingRequest = new DefaultProjectBuildingRequest(session);
        // rest of the code...
    }
}
```