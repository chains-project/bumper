```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo extends AbstractMojo {

    /**
     * @parameter default-value="${session}"
     * @required
     * @readonly
     */
    protected MavenSession session;

    /**
     * @parameter default-value="${project}"
     * @required
     * @readonly
     */
    protected MavenProject project;

    /**
     * @parameter default-value="${project.build.outputDirectory}"
     * @required
     * @readonly
     */
    protected File outputDirectory;

}
```