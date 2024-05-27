```java
import org.apache.maven.execution.MavenSession;
import org.codehaus.plexus.component.annotations.Requirement;

public void execute() {
    MavenSession session = getSession();
    MavenProject project = session.getCurrentProject();
    // ...
}
```