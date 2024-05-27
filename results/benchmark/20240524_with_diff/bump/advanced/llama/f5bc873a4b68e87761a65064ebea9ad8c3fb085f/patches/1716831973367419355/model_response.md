```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuildingRequest;

public void execute() {
    MavenSession session = MavenSessionFactory.getSession();
    ProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
    if (buildingRequest == null) {
        buildingRequest = new DefaultProjectBuildingRequest();
        session.getProjectBuildingRequest().setProjectBuildingRequest(buildingRequest);
    }
    MavenProject project = buildingRequest.getProject();
    // rest of the code
}
```