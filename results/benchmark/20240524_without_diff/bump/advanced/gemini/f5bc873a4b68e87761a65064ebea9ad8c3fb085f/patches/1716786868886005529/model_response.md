```java
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo extends AbstractMojo {

    /**
     * The Maven project.
     */
    @Parameter(defaultValue = "${project}", readonly = true, required = true)
    protected MavenProject project;

    // ...
}
```