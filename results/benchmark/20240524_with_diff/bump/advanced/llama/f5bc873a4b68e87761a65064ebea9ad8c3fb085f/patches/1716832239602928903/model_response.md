```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

public MavenProject getProject(MavenSession session) {
    DefaultProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
    return buildingRequest.getProject();
}
```