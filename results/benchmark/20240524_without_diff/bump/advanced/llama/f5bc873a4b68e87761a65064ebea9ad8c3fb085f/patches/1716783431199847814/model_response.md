```java
import org.apache.maven.execution.MavenSession;
import org.codehaus.plexus.component.annotations.Requirement;

public abstract class AbstractThemeMojo {
    @Requirement
    private MavenSession mavenSession;

    // ...
}
```