```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

MavenSession session = new MavenSession();
DefaultProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
MavenProject project = buildingRequest.getProject();
```