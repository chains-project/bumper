```java
import org.apache.maven.project.MavenProject;

public class AbstractThemeMojo {

    private final MavenProject project;

    public AbstractThemeMojo(MavenProject project) {
        this.project = project;
    }

    public MavenProject getProject() {
        return project;
    }
}
```