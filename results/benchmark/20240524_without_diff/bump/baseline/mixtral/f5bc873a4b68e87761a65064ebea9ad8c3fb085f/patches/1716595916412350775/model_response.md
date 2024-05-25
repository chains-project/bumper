Here is a proposed patch for the failing method:

```java
import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.factory.ArtifactFactory;
import org.apache.maven.artifact.metadata.ArtifactMetadataRetrievalException;
import org.apache.maven.artifact.resolver.ArtifactResolver;
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.component.configurator.expression.ExpressionEvaluationException;
import org.eclipse.aether.RepositorySystem;
import org.eclipse.aether.RepositorySystemSession;
import org.eclipse.aether.collection.CollectRequest;
import org.eclipse.aether.collection.CollectResult;
import org.eclipse.aether.graph.Dependency;
import org.eclipse.aether.graph.DependencyFilter;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactRequest;
import org.eclipse.aether.resolution.ArtifactResolutionException;
import org.eclipse.aether.resolution.ArtifactResult;
import org.eclipse.aether.util.filter.AndDependencyFilter;
import org.eclipse.aether.util.filter.ExclusionsDependencyFilter;
import org.eclipse.aether.util.filter.ScopeDependencyFilter;

import java.io.File;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Unpacks the theme files from the specified artifact into the specified directory.
 *
 * @author Martin Marinschek
 */
public class UnPackThemeMojo extends AbstractMojo {

  /**
   * The Maven project.
   *
   * @parameter expression="${project}"
   * @required
   * @readonly
   */
  private MavenProject project;

  /**
   * The Maven session.
   *
   * @parameter expression="${session}"
   * @required
   * @readonly
   */
  private MavenSession session;

  /**
   * The repository system.
   *
   * @parameter expression="${repositorySystem}"
   * @required
   * @readonly
   */
  private RepositorySystem repositorySystem;

  /**
   * The repository system session.
   *
   * @parameter expression="${repositorySystemSession}"
   * @required
   * @readonly
   */
  private RepositorySystemSession repositorySystemSession;

  /**
   * The local repository.
   *
   * @parameter expression="${localRepository}"
   * @required
   * @readonly
   */
  private ArtifactFactory artifactFactory;

  /**
   * The artifact resolver.
   *
   * @parameter expression="${localRepository}"
   * @required
   * @readonly
   */
  private ArtifactResolver artifactResolver;

  /**
   * The directory to which the files should be unpacked.
   *
   * @parameter default-value="${project.build.directory}/tobago-theme"
   */
  private File outputDirectory;

  /**
   * The artifact to unpack.
   *
   * @parameter
   */
  private Artifact artifact;

  @Override
  public void execute() throws MojoExecutionException, MojoFailureException {
    if ( artifact == null ) {
      throw new MojoExecutionException( "Artifact must be specified." );
    }

    if ( outputDirectory == null ) {
      throw new MojoExecutionException( "Output directory must be specified." );
    }

    if ( !outputDirectory.exists() ) {
      if ( !outputDirectory.mkdirs() ) {
        throw new MojoExecutionException( "Could not create output directory: " + outputDirectory );
      }
    }

    try {
      ArtifactResult artifactResult =
```