```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;

public class AbstractThemeMojo {

    private MavenSession session;

    private MavenProject project;

    public AbstractThemeMojo(MavenSession session, MavenProject project) {
        this.session = session;
        this.project = project;
    }

    public MavenSession getSession() {
        return session;
    }

    public MavenProject getProject() {
        return project;
    }
}
```