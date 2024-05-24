```java
  import org.apache.maven.artifact.Artifact;
  import org.apache.maven.artifact.DependencyResolutionRequiredException;
  import org.apache.maven.artifact.resolver.ArtifactResolutionRequest;
  import org.apache.maven.artifact.resolver.ArtifactResolutionResult;
  import org.apache.maven.artifact.resolver.ArtifactResolver;
  import org.apache.maven.execution.MavenSession;
  import org.apache.maven.model.Dependency;
  import org.apache.maven.plugin.MojoExecutionException;
  import org.apache.maven.plugin.MojoFailureException;
  import org.apache.maven.plugins.annotations.Component;
  import org.apache.maven.plugins.annotations.Mojo;
  import org.apache.maven.plugins.annotations.Parameter;
  import org.apache.maven.project.MavenProject;
  import org.apache.maven.project.artifact.ProjectArtifact;
  import org.apache.maven.repository.RepositorySystem;

  import java.io.File;
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.nio.file.Paths;
  import java.util.ArrayList;
  import java.util.Collections;
  import java.util.HashSet;
  import java.util.List;
  import java.util.Set;
  import java.util.function.Consumer;

  /**
   * Goal which unpacks the contents of a theme.
   *
   * @since 4.0.0
   */
  @Mojo(name = "unpack-theme", threadSafe = true)
  public class UnPackThemeMojo extends AbstractThemeMojo {

    /**
     * The Maven Project Object.
     */
    @Parameter(defaultValue = "${project}", readonly = true, required = true)
    protected MavenProject project;

    /**
     * The Maven Session Object.
     */
    @Parameter(defaultValue = "${session}", readonly = true, required = true)
    protected MavenSession session;

    /**
     * The Artifact Resolver.
     */
    @Component
    private ArtifactResolver artifactResolver;

    /**
     * The Repository System.
     */
    @Component
    private RepositorySystem repositorySystem;

    /**
     * The theme artifact.
     */
    @Parameter(defaultValue = "${project.artifact}", readonly = true, required = true)
    private Artifact artifact;

    /**
     * The theme dependencies.
     */
    @Parameter(defaultValue = "${project.dependencies}", readonly = true, required = true)
    private List<Dependency> dependencies;

    /**
     * The theme artifact.
     *
     * @since 4.0.0
     */
    @Parameter(defaultValue = "${project.build.directory}/tobago-theme", required = true)
    private File themeDirectory;

    /**
     * The target directory where to unpack the theme.
     *
     * @since 4.0.0
     */
    @Parameter(defaultValue = "${project.build.directory}/tobago-theme-unpack", required = true)
    private File unpackThemeDirectory;

    @Override
    public void execute() throws MojoExecutionException, MojoFailureException {
      unpackTheme(themeDirectory, unpackThemeDirectory);
    }

    /**
     * Unpack the theme.
     *
     * @param themeDirectory the theme directory
     * @param unpackThemeDirectory the target directory where to unpack the theme
     * @throws MojoExecutionException if an error occurs
     */
    protected void unpackTheme(final File themeDirectory, final File unpackThemeDirectory) throws MojoExecutionException {
      if (!themeDirectory.exists()) {
        throw new MojoExecutionException("theme directory does not exist: " + themeDirectory);
      }
      if (!unpackThemeDirectory.exists()) {
        unpackThemeDirectory.mkdirs();
      }
      // unpack the theme.jar
      final File themeJar = new File(themeDirectory, "theme.jar");
      if (!themeJar.exists()) {
        throw new MojoExecutionException("theme.jar not found: " + themeJar);
      }
      try {
        final Path themeJarPath = Paths.get(themeJar.toURI());
        final Path unpackThemeDirectoryPath = Paths.get(unpackThemeDirectory.toURI());
        Files.walk(themeJarPath)
            .filter(path -> !path.equals(themeJarPath))
            .forEach(path -> {
              try {
                final Path targetPath = unpackThemeDirectoryPath.resolve(themeJarPath.relativize(path));
                if (path.toFile().isFile()) {
                  Files.copy(path, targetPath);
                } else {
                  targetPath.toFile().mkdirs();
                }
              } catch (final IOException e) {
                throw new MojoExecutionException("Error while unpacking theme", e);
              }
            });
      } catch (final IOException e) {
        throw new MojoExecutionException("Error while unpacking theme", e);
      }

      // copy the theme resources
      final File themeResources = new File(themeDirectory, "theme-resources");
      if (themeResources.exists()) {
        try {
          Files.walk(themeResources.toPath())
              .filter(path -> !path.equals(themeResources.toPath()))
              .forEach(path -> {
                try {
                  final Path targetPath = unpackThemeDirectoryPath.resolve(themeResources.toPath().relativize(path));
                  if (path.toFile().isFile()) {
                    Files.copy(path, targetPath);
                  } else {
                    targetPath.toFile().mkdirs();
                  }
                } catch (final IOException e) {
                  throw new MojoExecutionException("Error while unpacking theme resources", e);
                }
              });
        } catch (final IOException e) {
          throw new MojoExecutionException("Error while unpacking theme resources", e);
        }
      }

      // copy the theme dependencies
      final List<Artifact> themeArtifacts = new ArrayList<>();
      themeArtifacts.add(artifact);
      for (final Dependency dependency : dependencies) {
        try {
          final ArtifactResolutionRequest request = new ArtifactResolutionRequest();
          request.setArtifact(artifactResolver.resolveArtifact(request).getArtifact());
          request.setResolveTransitively(true);
          request.setCollectionFilter(Collections.singletonList("jar"));
          final ArtifactResolutionResult result = artifactResolver.resolve(request);
          themeArtifacts.addAll(result.getArtifacts());
        } catch (final DependencyResolutionRequiredException e) {
          throw new MojoExecutionException("Error while resolving theme dependencies", e);
        }
      }

      for (final Artifact themeArtifact : themeArtifacts) {
        final File themeArtifactFile = themeArtifact.getFile();
        if (themeArtifactFile != null && themeArtifactFile.exists()) {
          try {
            final Path themeArtifactPath = Paths.get(themeArtifactFile.toURI());
            final Path unpackThemeDirectoryPath = Paths.get(unpackThemeDirectory.toURI());
            Files.walk(themeArtifactPath)
                .filter(path -> !path.equals(themeArtifactPath))
                .forEach(path -> {
                  try {
                    final Path targetPath = unpackThemeDirectoryPath.resolve(themeArtifactPath.relativize(path));
                    if (path.toFile().isFile()) {
                      Files.copy(path, targetPath);
                    } else {
                      targetPath.toFile().mkdirs();
                    }
                  } catch (final IOException e) {
                    throw new MojoExecutionException("Error while unpacking theme dependency", e);
                  }
                });
          } catch (final IOException e) {
            throw new MojoExecutionException("Error while unpacking theme dependency", e);
          }
        }
      }

      // unpack the theme lib
      final File themeLib = new File(themeDirectory, "theme-lib");
      if (themeLib.exists()) {
        try {
          Files.walk(themeLib.toPath())
              .filter(path -> !path.equals(themeLib.toPath()))
              .forEach(path -> {
                try {
                  final Path targetPath = unpackThemeDirectoryPath.resolve(themeLib.toPath().relativize(path));
                  if (path.toFile().isFile()) {
                    Files.copy(path, targetPath);
                  } else {
                    targetPath.toFile().mkdirs();
                  }
                } catch (final IOException e) {
                  throw new MojoExecutionException("Error while unpacking theme lib", e);
                }
              });
        } catch (final IOException e) {
          throw new MojoExecutionException("Error while unpacking theme lib", e);
        }
      }
    }
  }
```