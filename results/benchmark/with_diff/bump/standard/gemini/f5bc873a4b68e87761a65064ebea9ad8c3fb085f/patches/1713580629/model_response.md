```java
import org.apache.maven.execution.MavenSession;

public abstract class AbstractThemeMojo extends AbstractMyfacesMojo {

    /**
     * @parameter expression="${session}"
     * @required
     * @since 2.0.1
     */
    protected MavenSession session;

    protected MavenProject getProject() {
        return session.getCurrentProject();
    }

}
``` 
