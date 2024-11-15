Here is a proposed patch for the failing method:

```java
import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.ArtifactResolver;
import org.apache.maven.artifact.repository.ArtifactRepository;
import org.apache.maven.artifact.resolver.ArtifactResolutionException;
import org.apache.maven.artifact.resolver.ArtifactResolverException2;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.components.interactivity.Prompter;
import org.codehaus.plexus.util.FileUtils;
import org.eclipse.aether.RepositorySystem;
import org.eclipse.aether.RepositorySystemSession;
import org.eclipse.aether.collection.CollectRequest;
import org.eclipse.aether.collection.CollectResult;
import org.eclipse.aether.collection.DependencyCollectionException;
import org.eclipse.aether.graph.Dependency;
import org.eclipse.aether.graph.DependencyNode;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactResolutionException2;
import org.eclipse.aether.resolution.ArtifactResult;
import org.eclipse.aether.resolution.DependencyRequest;
import org.eclipse.aether.resolution.DependencyResolutionException;
import org.eclipse.aether.resolution.DependencyResolutionResult;
import org.eclipse.aether.resolution.ResourceResolver;
import org.eclipse.aether.util.artifact.JavaScopes;

/**
 * Unpacks the theme archive.
 *
 * @goal unpack-theme
 * @phase process-resources
 * @requiresDependencyResolution
 * @threadSafe
 */
public class UnPackThemeMojo extends AbstractMojo {

  /**
   * The Maven project.
   *
   * @parameter default-value="${project}"
   * @required
   * @readonly
   */
  private MavenProject project;

  /**
   * The Maven project build directory.
   *
   * @parameter default-value="${project.build.directory}/tobago-theme"
   * @required
   * @readonly
   */
  private File outputDirectory;

  /**
   * The theme archive file.
   *
   * @parameter expression="${theme}"
   * @required
   */
  private File theme;

  /**
   * The Maven repository.
   *
   * @parameter default-value="${project.remoteProjectRepositories}"
   * @required
   * @readonly
   */
  private List<RemoteRepository> remoteRepositories;

  /**
   * The Maven local repository.
   *
   * @parameter default-value="${localRepository}"
   * @required
   * @readonly
   */
  private ArtifactRepository localRepository;

  /**
   * The Maven repository system.
   *
   * @parameter default-value="${repositorySystem}"
   * @required
   * @readonly
   */
  private RepositorySystem repositorySystem;

  /**
   * The Maven repository system session.
   *
   * @parameter default-value="${repositorySystemSession}"
   * @required
   * @readonly
   */
  private RepositorySystemSession repositorySystemSession;

  /**
   * The Maven artifact resolver.
   *
   * @parameter default-value="${localRepositoryBasedResolver}"
   * @required
   * @readonly
   */
  private ArtifactResolver artifactResolver;

  /**
   * The Maven project build directory.
   *
   * @parameter default-value="${project.build.directory}"
   * @required
   * @readonly
   */
  private File buildDirectory;

  /**
   * The Maven project version.
   *
   * @parameter default-value="${project.version}"
   * @required
   * @readonly
   */
  private String version;

  /**
   * The Maven prompter.
   *
   * @parameter default-value="${prompter}"
   * @required
   * @readonly
   */
  private Prompter prompter;

  /**
   * The Maven resource resolver.
   *
   * @parameter default-value="${resourceResolver}"
   * @required
   * @readonly
   */
  private ResourceResolver resourceResolver;

  /**
   * Unpacks the theme archive.
   *
   * @throws MojoExecutionException if an error occurs
   */
  @Override
  public void execute() throws MojoExecutionException {

    try {
      final DependencyRequest request =
```