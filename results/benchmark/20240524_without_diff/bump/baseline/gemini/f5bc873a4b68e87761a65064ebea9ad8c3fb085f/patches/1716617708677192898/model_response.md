```java
  import org.apache.maven.artifact.DependencyResolutionRequiredException;

  import java.io.File;
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.nio.file.Paths;
  import java.util.List;
  import java.util.Map;
  import java.util.stream.Collectors;
  import java.util.zip.ZipEntry;
  import java.util.zip.ZipFile;

  import org.apache.maven.artifact.Artifact;
  import org.apache.maven.artifact.repository.ArtifactRepository;
  import org.apache.maven.artifact.resolver.ArtifactNotFoundException;
  import org.apache.maven.artifact.resolver.ArtifactResolutionException;
  import org.apache.maven.execution.MavenSession;
  import org.apache.maven.model.Resource;
  import org.apache.maven.plugin.AbstractMojo;
  import org.apache.maven.plugin.MojoExecutionException;
  import org.apache.maven.plugin.MojoFailureException;
  import org.apache.maven.plugins.annotations.Component;
  import org.apache.maven.plugins.annotations.Parameter;
  import org.apache.maven.project.MavenProject;
  import org.apache.maven.project.MavenProjectHelper;
  import org.apache.maven.shared.artifact.filter.collection.ArtifactFilterException;
  import org.apache.maven.shared.artifact.filter.collection.FilterArtifacts;
  import org.apache.maven.shared.dependency.graph.DependencyNode;
  import org.apache.maven.shared.utils.io.FileUtils;
  import org.codehaus.plexus.util.StringUtils;

  /**
   * Unpacks the theme from the Tobago core artifact into the target directory.
   *
   * @since 3.0.0
   */
  public class UnPackThemeMojo extends AbstractMojo {

    /**
     * The Maven project.
     */
    @Parameter(defaultValue = "${project}", readonly = true, required = true)
    private MavenProject project;

    /**
     * The Maven session.
     */
    @Parameter(defaultValue = "${session}", readonly = true, required = true)
    private MavenSession session;

    /**
     * The local repository.
     */
    @Parameter(defaultValue = "${localRepository}", readonly = true, required = true)
    private ArtifactRepository localRepository;

    /**
     * The remote repositories.
     */
    @Parameter(defaultValue = "${project.remoteArtifactRepositories}", readonly = true, required = true)
    private List<ArtifactRepository> remoteRepositories;

    /**
     * The Maven project helper.
     */
    @Component
    private MavenProjectHelper projectHelper;

    /**
     * The artifact filter.
     */
    @Component
    private FilterArtifacts filterArtifacts;

    /**
     * The theme name.
     */
    @Parameter(property = "tobago.theme", defaultValue = "tobago")
    private String theme;

    /**
     * The theme version.
     */
    @Parameter(property = "tobago.theme.version", defaultValue = "${project.version}")
    private String themeVersion;

    /**
     * The target directory.
     */
    @Parameter(defaultValue = "${project.build.directory}/tobago-theme", required = true)
    private File targetDirectory;

    /**
     * The resource directory.
     */
    @Parameter(defaultValue = "${project.build.directory}/tobago-theme-resources", required = true)
    private File resourceDirectory;

    /**
     * The list of resources to copy.
     */
    @Parameter
    private List<Resource> resources;

    @Override
    public void execute() throws MojoExecutionException, MojoFailureException {
      try {
        final Artifact artifact = getThemeArtifact();
        final File themeFile = artifact.getFile();
        final String themePath = String.format("META-INF/resources/tobago/theme/%s", theme);
        final String versionPath = String.format("%s-%s", theme, themeVersion);

        final Path themeDirectory = Paths.get(targetDirectory.toString(), versionPath);
        final Path resourceDirectoryPath = Paths.get(resourceDirectory.toString(), versionPath);

        FileUtils.deleteDirectory(themeDirectory.toFile());
        FileUtils.deleteDirectory(resourceDirectoryPath.toFile());

        Files.createDirectories(themeDirectory);
        Files.createDirectories(resourceDirectoryPath.toFile());

        try (final ZipFile zipFile = new ZipFile(themeFile)) {
          zipFile.stream()
              .filter(entry -> entry.getName().startsWith(themePath))
              .forEach(entry -> {
                final Path target = Paths.get(themeDirectory.toString(), entry.getName().substring(themePath.length()));
                try {
                  Files.copy(zipFile.getInputStream(entry), target);
                } catch (final IOException e) {
                  throw new MojoExecutionException("Error unpacking theme", e);
                }
              });
        }

        if (resources != null) {
          for (final Resource resource : resources) {
            final String resourcePath = resource.getDirectory() + "/" + resource.getTargetPath();
            final Path source = Paths.get(project.getBasedir().toString(), resourcePath);
            final Path target = Paths.get(resourceDirectoryPath.toString(), resource.getTargetPath());
            try {
              Files.copy(source, target);
            } catch (final IOException e) {
              throw new MojoExecutionException("Error copying resource", e);
            }
          }
        }

        projectHelper.addResource(project, resourceDirectoryPath.toString(), versionPath, List.of());
      } catch (final ArtifactResolutionException | ArtifactNotFoundException | DependencyResolutionRequiredException e) {
        throw new MojoExecutionException("Error resolving theme artifact", e);
      } catch (final IOException e) {
        throw new MojoExecutionException("Error unpacking theme", e);
      } catch (final ArtifactFilterException e) {
        throw new MojoExecutionException("Error filtering theme artifact", e);
      }
    }

    private Artifact getThemeArtifact()
        throws ArtifactResolutionException, ArtifactNotFoundException, DependencyResolutionRequiredException, ArtifactFilterException {
      final DependencyNode dependencyNode = project.getDependencyTree().getDependencies().stream()
          .filter(node -> "org.apache.myfaces.tobago".equals(node.getArtifact().getGroupId())
              && "tobago-core".equals(node.getArtifact().getArtifactId()))
          .findFirst()
          .orElseThrow(() -> new ArtifactNotFoundException("tobago-core"));

      final Artifact artifact = dependencyNode.getArtifact();
      artifact.setVersion(themeVersion);

      final List<Artifact> artifacts = filterArtifacts.filter(List.of(artifact), project, localRepository, remoteRepositories);
      if (artifacts.isEmpty()) {
        throw new ArtifactNotFoundException("tobago-core", themeVersion);
      }

      return artifacts.get(0);
    }
  }
```