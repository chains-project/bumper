```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingRequest;

public void execute() {
    MavenSession mavenSession = MavenSessionFactory.getSession();
    ProjectBuildingRequest buildingRequest = mavenSession.getProjectBuildingRequest();
    ProjectBuilder projectBuilder = mavenSession.getProjectBuilder();
    MavenProject mavenProject = projectBuilder.build(buildingRequest).getProject();
    // rest of the code
}
```