```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo extends AbstractMojo {

    /**
     * The Maven project.
     */
    @Parameter(defaultValue = "${project}", readonly = true, required = true)
    protected MavenProject project;

    /**
     * The Maven session.
     */
    @Parameter(defaultValue = "${session}", readonly = true, required = true)
    protected MavenSession session;

    // ...

}
```