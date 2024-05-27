```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.Project;

public void execute() {
    MavenSession session = MavenSessionFactory.getSession();
    Project project = session.getCurrentProject();
    // rest of the code
}
```