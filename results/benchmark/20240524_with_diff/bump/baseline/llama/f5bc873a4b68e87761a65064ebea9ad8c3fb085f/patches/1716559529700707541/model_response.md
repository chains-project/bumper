```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuilder;
import org.apache.maven.project.MavenProject;

public MavenProject getProject(MavenSession session) {
    return new DefaultProjectBuilder().build(session.getCurrentProject().getFile(), session);
}
```