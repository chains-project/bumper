```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

public void execute() {
    MavenSession session = MavenSessionFactory.getMavenSession();
    DefaultProjectBuildingRequest request = session.getProjectBuildingRequest();
    MavenProject project = request.getProject();
    // rest of the code
}
```