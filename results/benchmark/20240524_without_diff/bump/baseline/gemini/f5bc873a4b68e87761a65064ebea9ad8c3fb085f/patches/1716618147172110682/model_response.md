```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingException;
import org.apache.maven.project.ProjectBuildingRequest;
import org.apache.maven.project.ProjectBuildingResult;
import org.codehaus.plexus.component.annotations.Component;
import org.codehaus.plexus.component.annotations.Requirement;
import org.codehaus.plexus.logging.Logger;
import org.eclipse.aether.RepositorySystemSession;

import java.util.List;

/**
 * Abstract base class for all mojos that need to access the current Maven project.
 */
@Component(role = AbstractThemeMojo.class)
public abstract class AbstractThemeMojo extends AbstractMojo {

  /**
   * The Maven project.
   */
  @Requirement
  protected MavenProject project;

  @Requirement
  protected MavenSession session;

  @Requirement
  protected RepositorySystemSession repoSession;

  @Requirement
  protected ProjectBuilder projectBuilder;

  @Requirement
  protected Logger logger;

  /**
   * Returns the current Maven project.
   *
   * @return the current Maven project
   */
  protected MavenProject getMavenProject() {
    return project;
  }

  /**
   * Returns the current Maven project.
   *
   * @return the current Maven project
   * @throws ProjectBuildingException if the project cannot be built
   */
  protected MavenProject getMavenProjectFromSession() throws ProjectBuildingException {
    ProjectBuildingRequest request = new ProjectBuildingRequest();
    request.setRepositorySession(repoSession);
    request.setRemoteRepositories(session.getCurrentProject().getRemoteProjectRepositories());
    request.setProject(project);
    ProjectBuildingResult result = projectBuilder.build(request);
    return result.getProject();
  }

  /**
   * Returns the list of reactor projects.
   *
   * @return the list of reactor projects
   */
  protected List<MavenProject> getReactorProjects() {
    return session.getProjects();
  }

  /**
   * Returns the current Maven session.
   *
   * @return the current Maven session
   */
  protected MavenSession getMavenSession() {
    return session;
  }

  /**
   * Returns the current repository system session.
   *
   * @return the current repository system session
   */
  protected RepositorySystemSession getRepositorySystemSession() {
    return repoSession;
  }

  /**
   * Returns the current Maven logger.
   *
   * @return the current Maven logger
   */
  protected Logger getLogger() {
    return logger;
  }
}
```