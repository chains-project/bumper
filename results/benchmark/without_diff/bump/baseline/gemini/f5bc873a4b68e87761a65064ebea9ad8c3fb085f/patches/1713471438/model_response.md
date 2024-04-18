```java
  import org.apache.maven.artifact.DependencyResolutionRequiredException;
  import org.apache.maven.plugin.MojoExecutionException;
  import org.apache.maven.project.MavenProject;
  import org.apache.maven.shared.artifact.ArtifactCoordinate;
  import org.apache.myfaces.tobago.maven.plugin.AbstractThemeMojo;
  import org.apache.myfaces.tobago.maven.plugin.UnPackThemeMojo;

  import java.io.File;
  import java.io.IOException;
  import java.util.List;

  /**
   * Unpacks a theme to the target directory.
   *
   * @author Werner Punz (latest modification by $Author$)
   * @version $Revision$ $Date$
   */
  public class UnPackThemeMojo extends AbstractThemeMojo {

    /**
     * The theme to unpack.
     *
     * @parameter property="theme"
     * @required
     */
    private String theme;

    /**
     * The target directory.
     *
     * @parameter property="targetDirectory"
     * @required
     */
    private String targetDirectory;

    /**
     * The target directory.
     *
     * @parameter property="targetDirectory"
     * @required
     */
    private File targetDirectoryFile;

    /**
     * @parameter property="themeCoordinates"
     * @required
     */
    private List<ArtifactCoordinate> themeCoordinates;

    /**
     * @parameter property="themeVersion"
     * @required
     */
    private String themeVersion;

    /**
     * @parameter property="themeGroupId"
     * @required
     */
    private String themeGroupId;

    /**
     * @parameter property="themeArtifactId"
     * @required
     */
    private String themeArtifactId;

    /**
     * @parameter property="themeType"
     * @required
     */
    private String themeType;

    /**
     * @parameter property="themeClassifier"
     * @required
     */
    private String themeClassifier;

    @Override
    public void execute() throws MojoExecutionException {

      if (theme == null) {
        throw new MojoExecutionException("theme is null");
      }
      if (targetDirectory == null) {
        throw new MojoExecutionException("targetDirectory is null");
      }
      if (themeCoordinates == null) {
        throw new MojoExecutionException("themeCoordinates is null");
      }
      if (themeVersion == null) {
        throw new MojoExecutionException("themeVersion is null");
      }
      if (themeGroupId == null) {
        throw new MojoExecutionException("themeGroupId is null");
      }
      if (themeArtifactId == null) {
        throw new MojoExecutionException("themeArtifactId is null");
      }
      if (themeType == null) {
        throw new MojoExecutionException("themeType is null");
      }
      if (themeClassifier == null) {
        throw new MojoExecutionException("themeClassifier is null");
      }

      final MavenProject project = (MavenProject) getPluginContext().get("project");
      try {
        final File targetFile = getUnpackedThemeFile(project);
        if (!targetFile.exists()) {
          getLog().info("Unpacking theme " + theme + " to " + targetFile);
          getMavenArtifactManager().resolveTransitively(themeCoordinates, project.getRemoteArtifactRepositories(),
              project.getLocalRepository());
          getMavenArtifactManager().deploy(targetFile, themeGroupId, themeArtifactId, themeVersion, themeType, themeClassifier,
              project.getRemoteArtifactRepositories());
        }
      } catch (final DependencyResolutionRequiredException e) {
        throw new MojoExecutionException("Error resolving theme artifact: " + e.getMessage(), e);
      } catch (final IOException e) {
        throw new MojoExecutionException("Error unpacking theme: " + e.getMessage(), e);
      }
    }

    private File getUnpackedThemeFile(final MavenProject project) throws IOException {
      final File targetDirectoryFile = new File(project.getBuild().getDirectory(), targetDirectory);
      if (!targetDirectoryFile.exists()) {
        if (!targetDirectoryFile.mkdirs()) {
          throw new IOException("Cannot create directory " + targetDirectoryFile);
        }
      }
      return new File(targetDirectoryFile, theme + "-" + themeVersion + "." + themeType);
    }

  }
```