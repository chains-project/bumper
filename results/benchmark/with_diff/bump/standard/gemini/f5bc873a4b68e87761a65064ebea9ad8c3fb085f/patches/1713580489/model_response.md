```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo extends AbstractMojo {

  protected MavenSession session;

  public void execute() throws MojoExecutionException, MojoFailureException {
    session = (MavenSession) getPluginContext().get("session");
    MavenProject project = session.getCurrentProject();
    // ...
  }
}
```