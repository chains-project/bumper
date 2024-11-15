```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;
import org.apache.maven.settings.Settings;
import org.eclipse.aether.RepositorySystemSession;
import org.eclipse.aether.repository.RemoteRepository;

import java.util.List;

public abstract class AbstractThemeMojo extends AbstractTobagoMojo {

    /**
     * @parameter default-value="${session}"
     * @required
     * @readonly
     */
    protected MavenSession session;

    /**
     * @parameter default-value="${settings}"
     * @required
     * @readonly
     */
    protected Settings settings;

    /**
     * @parameter default-value="${repositorySystemSession}"
     * @required
     * @readonly
     */
    protected RepositorySystemSession repositorySystemSession;

    /**
     * @parameter default-value="${project}"
     * @required
     * @readonly
     */
    protected MavenProject project;

    /**
     * @parameter expression="${remoteRepositories}"
     * @required
     * @readonly
     */
    protected List<RemoteRepository> remoteRepositories;

    /**
     * @parameter default-value="${reactorProjects}"
     * @required
     * @readonly
     */
    protected List<MavenProject> reactorProjects;

    /**
     * @parameter default-value="${skip}"
     */
    protected boolean skip;

}
```