```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

public class AbstractThemeMojo {
    public void execute() {
        MavenSession mavenSession = new MavenSession();
        DefaultProjectBuildingRequest request = mavenSession.getProjectBuildingRequest();
        // rest of the code
    }
}
```