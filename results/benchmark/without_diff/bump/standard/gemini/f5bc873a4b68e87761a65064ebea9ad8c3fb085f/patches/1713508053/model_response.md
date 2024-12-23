```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo extends AbstractMyfacesMojo {

    /**
     * The current Maven session.
     *
     * @since 3.0.0
     */
    ++@Parameter(defaultValue = "${session}", readonly = true, required = true)
    private MavenSession session;

    /**
     * The Maven project.
     *
     * @since 1.0.0
     */
    ++@Parameter(defaultValue = "${project}", readonly = true, required = true)
    private MavenProject project;

    public MavenProject getProject() {
        return project;
    }

    public MavenSession getSession() {
        return session;
    }
}
```