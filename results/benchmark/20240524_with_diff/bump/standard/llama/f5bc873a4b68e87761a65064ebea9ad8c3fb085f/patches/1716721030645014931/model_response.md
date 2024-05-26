```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuildingRequest;

public void execute() {
    ProjectBuildingRequest buildingRequest = new DefaultProjectBuildingRequest();
    MavenSession mavenSession = new MavenSession();
    buildingRequest.setProcessPlugins(false);
    MavenProject mavenProject = mavenSession.getCurrentProject();
    // rest of the code
}
```