```java
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo {

    private final MavenProject project;

    public AbstractThemeMojo(MavenProject project) {
        this.project = project;
    }

    // ...
}
```