```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultMavenProjectCache;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingRequest;

public void execute() {
    ProjectBuildingRequest buildingRequest = new ProjectBuildingRequest();
    MavenSession session = new MavenSession();
    buildingRequest.setProcessPlugins(false);
    ProjectBuilder projectBuilder = session.getProjectBuilder();
    MavenProject project = projectBuilder.build(buildingRequest).getProject();
    // rest of the code
}
```