```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

public void execute() {
    MavenSession session = MavenSessionFactory.getSession();
    DefaultProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
    MavenProject project = buildingRequest.getProject();
    // rest of the code
}
```