```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuildingRequest;

MavenSession session = new MavenSession();
ProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
```