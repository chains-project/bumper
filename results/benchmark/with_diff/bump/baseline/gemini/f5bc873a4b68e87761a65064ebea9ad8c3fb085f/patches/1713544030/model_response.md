```java
import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.repository.ArtifactRepository;
import org.apache.maven.artifact.resolver.ArtifactResolutionResult;
import org.apache.maven.artifact.resolver.ArtifactResolver;
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Component;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.MavenProjectHelper;
import org.apache.maven.shared.artifact.resolve.ArtifactResolverException;
import org.apache.maven.shared.artifact.resolve.ArtifactResult;
import org.apache.maven.shared.utils.io.FileUtils;
import org.apache.maven.shared.utils.xml.Xpp3Dom;
import org.codehaus.plexus.util.StringUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

/**
 * Goal which unpacks the theme to the target directory.
 */
@Mojo(name = "unpack-theme", threadSafe = true)
public class UnPackThemeMojo extends AbstractThemeMojo {

  /**
   * The maven project.
   */
  @Parameter(defaultValue = "${project}", readonly = true)
  private MavenProject project;

  /**
   * The maven session.
   */
  @Parameter(defaultValue = "${session}", readonly = true)
  private MavenSession session;

  /**
   * The maven project helper.
   */
  @Component
  private MavenProjectHelper projectHelper;

  /**
   * The artifact resolver.
   */
  @Component
  private ArtifactResolver artifactResolver;

  /**
   * The local repository.
   */
  @Parameter(defaultValue = "${localRepository}", readonly = true)
  private ArtifactRepository localRepository;

  /**
   * The remote repositories.
   */
  @Parameter(defaultValue = "${project.remoteArtifactRepositories}", readonly = true)
  private List<ArtifactRepository> remoteRepositories;

  /**
   * The theme artifact.
   */
  @Parameter(required = true)
  private Artifact themeArtifact;

  /**
   * The unpacked theme artifact.
   */
  @Parameter(defaultValue = "${project.build.directory}/unpacked-theme", required = true)
  private File unpackedThemeArtifact;

  /**
   * The skip unpack flag.
   */
  @Parameter(property = "tobago.theme.unpack.skip", defaultValue = "false")
  private boolean skipUnpack;

  @Override
  public void execute() throws MojoExecutionException, MojoFailureException {
    if (skipUnpack) {
      getLog().info("Skipping unpack-theme.");
      return;
    }

    if (StringUtils.isEmpty(themeArtifact.getGroupId()) || StringUtils.isEmpty(themeArtifact.getArtifactId())) {
      throw new MojoExecutionException("Theme artifactId or groupId is missing.");
    }

    try {
      final ArtifactResult artifactResult = artifactResolver.resolveArtifact(project, themeArtifact,
          localRepository, remoteRepositories);

      if (artifactResult != null && artifactResult.getArtifact() != null) {
        final Artifact resolvedThemeArtifact = artifactResult.getArtifact();

        // unpack the theme to the target directory
        FileUtils.copyFile(resolvedThemeArtifact.getFile(), unpackedThemeArtifact);
      }
    } catch (ArtifactResolverException e) {
      throw new MojoExecutionException("Error resolving theme artifact.", e);
    } catch (IOException e) {
      throw new MojoExecutionException("Error unpacking theme artifact.", e);
    }
  }
}
```