```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingRequest;
import org.codehaus.plexus.component.annotations.Component;

@Component(role = ProjectBuilder.class)
public class MyProjectBuilder extends ProjectBuilder {
    @Override
    public MavenProject build(ProjectBuildingRequest request) {
        MavenSession session = request.getMavenSession();
        MavenProject project = session.getCurrentProject();
        return project;
    }
}
```