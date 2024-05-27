```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.AbstractMojo;

public abstract class AbstractThemeMojo extends AbstractMojo {
    protected MavenSession session;

    public AbstractThemeMojo() {
        this.session = getPluginContext().getMavenSession();
    }
}
```