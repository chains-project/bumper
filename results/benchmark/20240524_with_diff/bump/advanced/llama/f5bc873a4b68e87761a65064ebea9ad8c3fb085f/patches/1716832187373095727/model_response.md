```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingRequest;

public abstract class AbstractThemeMojo {
    public void execute() {
        MavenSession mavenSession = new MavenSession();
        ProjectBuildingRequest buildingRequest = new DefaultProjectBuildingRequest(mavenSession);
        ProjectBuilder projectBuilder = mavenSession.getProjectBuilder();
        projectBuilder.build(buildingRequest);
    }
}
```