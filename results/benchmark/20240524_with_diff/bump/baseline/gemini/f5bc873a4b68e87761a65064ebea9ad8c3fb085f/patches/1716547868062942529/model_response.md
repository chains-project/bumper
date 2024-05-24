```java
import org.apache.maven.artifact.versioning.InvalidVersionSpecificationException;
import org.apache.maven.artifact.versioning.VersionRange;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.artifact.ProjectArtifactMetadata;
import org.codehaus.plexus.util.StringUtils;
import org.eclipse.aether.artifact.Artifact;
import org.eclipse.aether.artifact.DefaultArtifact;

import java.util.ArrayList;
import java.util.List;

/**
 * Unpacks a theme.
 */
@Mojo(name = "unpack-theme", threadSafe = true)
public class UnPackThemeMojo extends AbstractThemeMojo {

  /**
   * The version range of the theme to unpack.
   */
  @Parameter(property = "themeVersion", defaultValue = "${project.version}")
  private String themeVersion;

  /**
   * The classifier of the theme to unpack.
   */
  @Parameter(property = "themeClassifier")
  private String themeClassifier;

  /**
   * The type of the theme to unpack.
   */
  @Parameter(property = "themeType", defaultValue = "war")
  private String themeType;

  /**
   * The Maven project.
   */
  @Parameter(defaultValue = "${project}", readonly = true)
  private MavenProject project;

  /**
   * Unpacks a theme.
   *
   * @throws MojoExecutionException if an error occurs during the execution.
   * @throws MojoFailureException   if the execution fails.
   */
  @Override
  public void execute() throws MojoExecutionException, MojoFailureException {

    final Artifact artifact = new DefaultArtifact(
        project.getGroupId(),
        project.getArtifactId(),
        themeVersion,
        themeClassifier,
        themeType);

    final Artifact themeArtifact;
    try {
      themeArtifact = projectHelper.resolveArtifact(artifact);
    } catch (final InvalidVersionSpecificationException e) {
      throw new MojoExecutionException(e.getMessage(), e);
    }

    final List<Artifact> artifacts = new ArrayList<>();
    artifacts.add(themeArtifact);

    final ProjectArtifactMetadata metadata = project.getArtifact().getMetadata();
    final VersionRange versionRange = VersionRange.createFromVersionSpec(metadata.getVersion());

    final List<Artifact> unpackArtifacts = new ArrayList<>();
    for (final Artifact artifact1 : artifacts) {
      if (versionRange.containsVersion(artifact1.getVersion())) {
        unpackArtifacts.add(artifact1);
      }
    }

    if (unpackArtifacts.isEmpty()) {
      throw new MojoExecutionException("No theme found for version: " + themeVersion);
    }

    if (unpackArtifacts.size() > 1) {
      throw new MojoExecutionException("Multiple themes found for version: " + themeVersion);
    }

    final Artifact themeUnpackArtifact = unpackArtifacts.get(0);

    final String themeUnpackPath = StringUtils.replace(themeUnpackArtifact.getFile().getAbsolutePath(),
        project.getBuild().getOutputDirectory(),
        project.getBuild().getDirectory());

    getLog().info("Unpacking theme: " + themeUnpackArtifact.getFile().getAbsolutePath());

    projectHelper.attachArtifact(project, themeUnpackArtifact, "theme");

    final File themeUnpackFile = new File(themeUnpackPath);
    if (themeUnpackFile.exists()) {
      getLog().info("Theme already unpacked: " + themeUnpackPath);
      return;
    }

    try {
      projectHelper.unpack(themeUnpackArtifact, project.getBasedir());
    } catch (final Exception e) {
      throw new MojoExecutionException("Error unpacking theme: " + themeUnpackArtifact.getFile().getAbsolutePath(), e);
    }
  }
}
```