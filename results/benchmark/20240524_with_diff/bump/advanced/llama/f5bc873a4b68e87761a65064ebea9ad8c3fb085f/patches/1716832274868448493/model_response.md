```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

public void execute() {
    MavenSession mavenSession = MavenSessionFactory.getSession();
    DefaultProjectBuildingRequest buildingRequest = mavenSession.getProjectBuildingRequest();
    MavenProject mavenProject = buildingRequest.getProject();
    // rest of the code
}
```