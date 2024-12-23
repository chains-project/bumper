```java
import org.apache.maven.artifact.versioning.ArtifactVersion;
import org.apache.maven.artifact.versioning.DefaultArtifactVersion;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Unpack a theme from a WAR file and create a new WAR file with the theme as a JAR file.
 */
@Mojo(name = "unpack-theme", threadSafe = true)
public class UnPackThemeMojo extends AbstractThemeMojo {

  /**
   * The version of the Tobago API.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoApiVersion;

  /**
   * The version of the Tobago Core.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoCoreVersion;

  /**
   * The version of the Tobago Integration.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoIntegrationVersion;

  /**
   * The version of the Tobago TLD.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoTldVersion;

  /**
   * The version of the Tobago Widget.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoWidgetVersion;

  /**
   * The version of the Tobago Demo.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoDemoVersion;

  /**
   * The version of the Tobago Example.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoExampleVersion;

  /**
   * The version of the Tobago Quickstart.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoQuickstartVersion;

  /**
   * The version of the Tobago Showcase.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoShowcaseVersion;

  /**
   * The version of the Tobago Test.
   */
  @Parameter(defaultValue = "4.10.0")
  private String tobagoTestVersion;

  @Override
  public void execute() throws MojoExecutionException {

    final File warFile = new File(project.getBuild().getDirectory(), project.getBuild().getFinalName() + ".war");
    final File themeDir = new File(project.getBuild().getDirectory(), "theme");
    final File themeJar = new File(project.getBuild().getDirectory(), project.getBuild().getFinalName() + "-theme.jar");

    try {
      // Unpack the WAR file
      unpackWar(warFile, themeDir);

      // Create a JAR file from the theme directory
      createJar(themeDir, themeJar);

      // Update the WAR file with the theme JAR file
      updateWar(warFile, themeJar);

      // Update the project's dependencies
      updateDependencies();

    } catch (IOException e) {
      throw new MojoExecutionException("Failed to unpack theme", e);
    }
  }

  private void updateDependencies() {
    final ArtifactVersion tobagoApiVersion = new DefaultArtifactVersion(this.tobagoApiVersion);
    final ArtifactVersion tobagoCoreVersion = new DefaultArtifactVersion(this.tobagoCoreVersion);
    final ArtifactVersion tobagoIntegrationVersion = new DefaultArtifactVersion(this.tobagoIntegrationVersion);
    final ArtifactVersion tobagoTldVersion = new DefaultArtifactVersion(this.tobagoTldVersion);
    final ArtifactVersion tobagoWidgetVersion = new DefaultArtifactVersion(this.tobagoWidgetVersion);
    final ArtifactVersion tobagoDemoVersion = new DefaultArtifactVersion(this.tobagoDemoVersion);
    final ArtifactVersion tobagoExampleVersion = new DefaultArtifactVersion(this.tobagoExampleVersion);
    final ArtifactVersion tobagoQuickstartVersion = new DefaultArtifactVersion(this.tobagoQuickstartVersion);
    final ArtifactVersion tobagoShowcaseVersion = new DefaultArtifactVersion(this.tobagoShowcaseVersion);
    final ArtifactVersion tobagoTestVersion = new DefaultArtifactVersion(this.tobagoTestVersion);

    // Update the project's dependencies
    project.getDependencies().stream()
        .filter(dependency -> dependency.getGroupId().equals("org.apache.myfaces.tobago"))
        .forEach(dependency -> {
          switch (dependency.getArtifactId()) {
            case "tobago-api":
              dependency.setVersion(tobagoApiVersion.toString());
              break;
            case "tobago-core":
              dependency.setVersion(tobagoCoreVersion.toString());
              break;
            case "tobago-integration":
              dependency.setVersion(tobagoIntegrationVersion.toString());
              break;
            case "tobago-tld":
              dependency.setVersion(tobagoTldVersion.toString());
              break;
            case "tobago-widget":
              dependency.setVersion(tobagoWidgetVersion.toString());
              break;
            case "tobago-demo":
              dependency.setVersion(tobagoDemoVersion.toString());
              break;
            case "tobago-example":
              dependency.setVersion(tobagoExampleVersion.toString());
              break;
            case "tobago-quickstart":
              dependency.setVersion(tobagoQuickstartVersion.toString());
              break;
            case "tobago-showcase":
              dependency.setVersion(tobagoShowcaseVersion.toString());
              break;
            case "tobago-test":
              dependency.setVersion(tobagoTestVersion.toString());
              break;
          }
        });
  }

  private void updateWar(File warFile, File themeJar) throws IOException {
    final Path warPath = Paths.get(warFile.getAbsolutePath());
    final Path themeJarPath = Paths.get(themeJar.getAbsolutePath());

    // Remove the theme directory from the WAR file
    Files.walk(warPath)
        .filter(path -> path.toString().endsWith(".jar"))
        .forEach(path -> {
          try {
            Files.delete(path);
          } catch (IOException e) {
            getLog().error("Failed to delete " + path, e);
          }
        });

    // Add the theme JAR file to the WAR file
    Files.copy(themeJarPath, warPath.resolve(themeJar.getName()));
  }

  private void createJar(File themeDir, File themeJar) throws IOException {
    final Path themeDirPath = Paths.get(themeDir.getAbsolutePath());
    final Path themeJarPath = Paths.get(themeJar.getAbsolutePath());

    // Create a JAR file from the theme directory
    Files.createFile(themeJarPath);
    Files.walk(themeDirPath)
        .filter(path -> !path.equals(themeDirPath))
        .forEach(path -> {
          try {
            Files.copy(path, themeJarPath.resolve(themeDirPath.relativize(path)));
          } catch (IOException e) {
            getLog().error("Failed to copy " + path, e);
          }
        });
  }

  private void unpackWar(File warFile, File themeDir) throws IOException {
    final Path warPath = Paths.get(warFile.getAbsolutePath());
    final Path themeDirPath = Paths.get(themeDir.getAbsolutePath());

    // Create the theme directory
    Files.createDirectories(themeDirPath);

    // Unpack the WAR file
    Files.walk(warPath)
        .filter(path -> path.toString().endsWith(".jar"))
        .forEach(path -> {
          try {
            Files.copy(path, themeDirPath.resolve(path.getFileName()));
          } catch (IOException e) {
            getLog().error("Failed to copy " + path, e);
          }
        });
  }
}
```