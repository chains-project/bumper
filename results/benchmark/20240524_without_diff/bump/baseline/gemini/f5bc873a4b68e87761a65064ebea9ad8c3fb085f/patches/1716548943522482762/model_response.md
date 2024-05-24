```java
  import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.resolver.ArtifactResolutionRequest;
import org.apache.maven.artifact.resolver.ArtifactResolutionResult;
import org.apache.maven.execution.MavenSession;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Component;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;
import org.apache.maven.repository.RepositorySystem;
import org.apache.maven.shared.artifact.filter.collection.ArtifactFilterException;
import org.apache.maven.shared.artifact.filter.collection.ArtifactsFilter;
import org.apache.maven.shared.artifact.filter.collection.FilterArtifacts;
import org.apache.maven.shared.transfer.artifact.resolve.ArtifactResolver;
import org.apache.maven.shared.transfer.artifact.resolve.ArtifactResolverException;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

import static org.apache.maven.shared.artifact.filter.collection.FilterArtifacts.filterArtifacts;

/**
 * Unpacks the theme jar into the target directory.
 */
public class UnPackThemeMojo extends AbstractThemeMojo {

  public static final String GOAL = "unpack-theme";

  /**
   * The Maven Session Object.
   */
  @Parameter(defaultValue = "${session}", readonly = true, required = true)
  private MavenSession session;

  /**
   * The Maven Project Object.
   */
  @Parameter(defaultValue = "${project}", readonly = true, required = true)
  private MavenProject project;

  /**
   * The artifact resolver.
   */
  @Component
  private ArtifactResolver artifactResolver;

  /**
   * The artifact filter.
   */
  @Component
  private FilterArtifacts filterArtifacts;

  /**
   * The repository system.
   */
  @Component
  private RepositorySystem repositorySystem;

  /**
   * The unpacked theme directory.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme", required = true)
  private File themeDirectory;

  /**
   * The unpacked theme jar file.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme.jar", required = true)
  private File themeJarFile;

  /**
   * The unpacked theme source directory.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-src", required = true)
  private File themeSourceDirectory;

  /**
   * The unpacked theme source jar file.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-src.jar", required = true)
  private File themeSourceJarFile;

  /**
   * The unpacked theme source directory.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-test", required = true)
  private File themeTestDirectory;

  /**
   * The unpacked theme source jar file.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-test.jar", required = true)
  private File themeTestJarFile;

  /**
   * The unpacked theme webapp directory.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-webapp", required = true)
  private File themeWebappDirectory;

  /**
   * The artifact to unpack.
   */
  @Parameter(defaultValue = "${project.artifactId}", required = true)
  private String artifactId;

  /**
   * The version of the artifact to unpack.
   */
  @Parameter(defaultValue = "${project.version}", required = true)
  private String version;

  /**
   * The type of the artifact to unpack.
   */
  @Parameter(defaultValue = "jar", required = true)
  private String type;

  /**
   * The classifier of the artifact to unpack.
   */
  @Parameter(defaultValue = "tobago-theme", required = true)
  private String classifier;

  /**
   * The scope of the artifact to unpack.
   */
  @Parameter(defaultValue = "compile", required = true)
  private String scope;

  /**
   * The classifier of the artifact to unpack.
   */
  @Parameter(defaultValue = "tobago-theme-src", required = true)
  private String classifierSrc;

  /**
   * The scope of the artifact to unpack.
   */
  @Parameter(defaultValue = "compile", required = true)
  private String scopeSrc;

  /**
   * The classifier of the artifact to unpack.
   */
  @Parameter(defaultValue = "tobago-theme-test", required = true)
  private String classifierTest;

  /**
   * The scope of the artifact to unpack.
   */
  @Parameter(defaultValue = "test", required = true)
  private String scopeTest;

  /**
   * The classifier of the artifact to unpack.
   */
  @Parameter(defaultValue = "tobago-theme-webapp", required = true)
  private String classifierWebapp;

  /**
   * The scope of the artifact to unpack.
   */
  @Parameter(defaultValue = "provided", required = true)
  private String scopeWebapp;

  /**
   * The path to the theme jar.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme.jar", required = true)
  private String themeJarPath;

  /**
   * The path to the theme source jar.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-src.jar", required = true)
  private String themeSourceJarPath;

  /**
   * The path to the theme test jar.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-test.jar", required = true)
  private String themeTestJarPath;

  /**
   * The path to the theme webapp jar.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-webapp.jar", required = true)
  private String themeWebappJarPath;

  /**
   * The path to the theme source directory.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-src", required = true)
  private String themeSourcePath;

  /**
   * The path to the theme test directory.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-test", required = true)
  private String themeTestPath;

  /**
   * The path to the theme webapp directory.
   */
  @Parameter(defaultValue = "${project.build.directory}/tobago-theme-webapp", required = true)
  private String themeWebappPath;

  /**
   * The list of filters for the webapp.
   */
  @Parameter
  private List<String> webappIncludes = Collections.singletonList("**/*");

  /**
   * The list of filters for the webapp.
   */
  @Parameter
  private List<String> webappExcludes = Collections.singletonList("**/META-INF/**");

  @Override
  public void execute() throws MojoExecutionException, MojoFailureException {

    final Artifact artifact = project.getArtifact();
    artifact.setArtifactId(artifactId);
    artifact.setVersion(version);
    artifact.setType(type);
    artifact.setClassifier(classifier);
    artifact.setScope(scope);

    final Artifact artifactSrc = project.getArtifact();
    artifactSrc.setArtifactId(artifactId);
    artifactSrc.setVersion(version);
    artifactSrc.setType(type);
    artifactSrc.setClassifier(classifierSrc);
    artifactSrc.setScope(scopeSrc);

    final Artifact artifactTest = project.getArtifact();
    artifactTest.setArtifactId(artifactId);
    artifactTest.setVersion(version);
    artifactTest.setType(type);
    artifactTest.setClassifier(classifierTest);
    artifactTest.setScope(scopeTest);

    final Artifact artifactWebapp = project.getArtifact();
    artifactWebapp.setArtifactId(artifactId);
    artifactWebapp.setVersion(version);
    artifactWebapp.setType(type);
    artifactWebapp.setClassifier(classifierWebapp);
    artifactWebapp.setScope(scopeWebapp);

    final List<Artifact> artifacts = new ArrayList<>();
    artifacts.add(artifact);
    artifacts.add(artifactSrc);
    artifacts.add(artifactTest);
    artifacts.add(artifactWebapp);

    final ArtifactResolutionRequest request = new ArtifactResolutionRequest()
        .setArtifactDependencies(artifacts)
        .setResolveTransitively(false)
        .setLocalRepository(session.getLocalRepository())
        .setRemoteRepositories(project.getRemoteArtifactRepositories());

    final ArtifactResolutionResult result;
    try {
      result = artifactResolver.resolve(request);
    } catch (ArtifactResolverException e) {
      throw new MojoExecutionException("Can't resolve artifacts", e);
    }

    final Collection<Artifact> resolvedArtifacts = result.getArtifacts();
    if (resolvedArtifacts.size() != artifacts.size()) {
      throw new MojoExecutionException("Can't resolve all artifacts");
    }

    final List<Artifact> resolvedArtifactsToUnpack = new ArrayList<>();
    for (final Artifact resolvedArtifact : resolvedArtifacts) {
      if (resolvedArtifact.getClassifier() != null) {
        resolvedArtifactsToUnpack.add(resolvedArtifact);
      }
    }

    final ArtifactsFilter artifactsFilter = new ArtifactsFilter();
    artifactsFilter.addInclude(webappIncludes);
    artifactsFilter.addExclude(webappExcludes);

    for (final Artifact resolvedArtifact : resolvedArtifactsToUnpack) {
      final File targetDirectory;
      switch (resolvedArtifact.getClassifier()) {
        case classifierSrc:
          targetDirectory = themeSourceDirectory;
          break;
        case classifierTest:
          targetDirectory = themeTestDirectory;
          break;
        case classifierWebapp:
          targetDirectory = themeWebappDirectory;
          break;
        default:
          targetDirectory = themeDirectory;
          break;
      }

      final List<Artifact> filteredArtifacts;
      try {
        filteredArtifacts = filterArtifacts(Collections.singletonList(resolvedArtifact), artifactsFilter,
            repositorySystem, session.getLocalRepository(), project.getRemoteArtifactRepositories());
      } catch (ArtifactFilterException e) {
        throw new MojoExecutionException("Can't filter artifacts", e);
      }

      if (filteredArtifacts.isEmpty()) {
        throw new MojoExecutionException("No artifacts to unpack");
      }

      final Artifact filteredArtifact = filteredArtifacts.get(0);
      if (!filteredArtifact.getFile().exists()) {
        throw new MojoExecutionException("Artifact to unpack doesn't exist");
      }

      final File targetFile = new File(targetDirectory, resolvedArtifact.getFile().getName());
      try {
        FileUtils.copyFile(filteredArtifact.getFile(), targetFile);
      } catch (IOException e) {
        throw new MojoExecutionException("Can't copy artifact", e);
      }
    }
  }
}
```