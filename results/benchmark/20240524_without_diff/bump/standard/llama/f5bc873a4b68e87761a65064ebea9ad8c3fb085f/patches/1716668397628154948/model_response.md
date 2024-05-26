```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;

public abstract class AbstractThemeMojo extends AbstractMojo {
    protected MavenSession mavenSession;

    public abstract void execute() throws MojoExecutionException, MojoFailureException;
}
```