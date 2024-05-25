```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuildingRequest;

public class AbstractThemeMojo {
    public void execute() {
        MavenSession mavenSession = new MavenSession();
        ProjectBuildingRequest buildingRequest = new DefaultProjectBuildingRequest(mavenSession);
    }
}
```