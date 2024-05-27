```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.AbstractMojo;

public abstract class AbstractThemeMojo extends AbstractMojo {
    protected MavenSession mavenSession;

    public AbstractThemeMojo() {}

    public AbstractThemeMojo(MavenSession mavenSession) {
        this.mavenSession = mavenSession;
    }
}
```