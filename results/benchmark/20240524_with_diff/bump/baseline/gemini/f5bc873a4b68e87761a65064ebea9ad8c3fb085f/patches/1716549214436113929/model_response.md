```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.model.Model;
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo extends AbstractMojo {

  @Parameter(defaultValue = "${session}", required = true, readonly = true)
  private MavenSession session;

  /**
   * The Maven project.
   */
  @Parameter(defaultValue = "${project}", required = true, readonly = true)
  private MavenProject project;

  /**
   * The current model.
   */
  @Parameter(defaultValue = "${project.model}", required = true, readonly = true)
  private Model model;

  public MavenSession getSession() {
    return session;
  }

  public MavenProject getProject() {
    return project;
  }

  public Model getModel() {
    return model;
  }
}
```