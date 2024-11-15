```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.execution.ProjectDependencyGraph;
import org.apache.maven.project.MavenProject;
import org.apache.maven.shared.dependency.graph.DependencyNode;

import java.util.List;
import java.util.Set;

public abstract class AbstractThemeMojo extends AbstractMojo {

  /**
   * @parameter expression="${session}"
   * @required
   * @readonly
   */
  protected MavenSession session;

  /**
   * The dependency graph.
   *
   * @parameter expression="${projectDependencyGraph}"
   * @required
   * @readonly
   */
  protected ProjectDependencyGraph projectDependencyGraph;

  protected List<MavenProject> findThemeProjects() {
    Set<DependencyNode> dependencyNodes = projectDependencyGraph.getSortedNodes(true);

    for (DependencyNode dependencyNode : dependencyNodes) {
      MavenProject project = dependencyNode.getArtifact().getProject();
      if (project != null && isThemeProject(project)) {
        return Collections.singletonList(project);
      }
    }

    return Collections.emptyList();
  }

  private boolean isThemeProject(MavenProject project) {
    for (String packaging : project.getPackagingList()) {
      if ("tobago-theme".equals(packaging)) {
        return true;
      }
    }
    return false;
  }
}
```