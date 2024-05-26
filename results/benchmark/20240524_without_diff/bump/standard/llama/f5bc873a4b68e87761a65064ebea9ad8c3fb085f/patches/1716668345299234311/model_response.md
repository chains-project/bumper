```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;

public abstract class AbstractThemeMojo extends AbstractMojo {
    protected MavenSession mavenSession;
    
    public abstract void execute() throws MojoExecutionException {
        // your code here
    }
}
```