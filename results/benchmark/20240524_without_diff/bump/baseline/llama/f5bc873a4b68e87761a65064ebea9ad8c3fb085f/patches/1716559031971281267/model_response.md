```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuildingRequest;

MavenSession session = MavenSessionFactory.getMavenSession();
ProjectBuildingRequest buildingRequest = session.getProjectBuildingRequest();
MavenProject project = buildingRequest.getProject();
```