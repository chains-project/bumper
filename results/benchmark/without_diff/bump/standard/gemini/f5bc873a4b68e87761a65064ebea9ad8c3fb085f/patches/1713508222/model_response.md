```java
import org.apache.maven.project.MavenProject;

public class AbstractThemeMojo {

    public void execute() {
        MavenProject project = (MavenProject) getPluginContext().get("project");
        // ...
    }
}
```