```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

public class AbstractThemeMojo {
    public void execute() {
        MavenSession session = new MavenSession();
        DefaultProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
        // Rest of the method
    }
}
```