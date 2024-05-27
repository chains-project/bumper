```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.AbstractMojo;

public class AbstractThemeMojo extends AbstractMojo {
    public void execute() {
        MavenSession mavenSession = MavenSessionFactory.getMavenSession();
        // rest of the code
    }
}
```