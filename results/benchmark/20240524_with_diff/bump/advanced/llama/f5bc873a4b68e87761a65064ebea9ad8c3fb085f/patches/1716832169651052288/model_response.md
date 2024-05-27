```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.Project;

public void execute() {
    MavenSession mavenSession = MavenPluginManager.getMavenSession();
    Project project = mavenSession.getCurrentProject();
    // rest of the method
}
```