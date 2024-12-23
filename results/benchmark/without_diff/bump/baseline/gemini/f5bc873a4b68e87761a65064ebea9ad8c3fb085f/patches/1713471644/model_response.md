```java
  import org.apache.maven.artifact.DependencyResolutionRequiredException;
  import org.apache.maven.plugin.MojoExecutionException;
  import org.apache.maven.plugins.annotations.Mojo;
  import org.apache.maven.plugins.annotations.Parameter;
  import org.apache.maven.project.MavenProject;

  import java.io.File;
  import java.io.IOException;

  /**
   * Unpack the theme resources from the theme WAR file.
   */
  @Mojo(name = "unpack-theme", requiresDependencyResolution = ResolutionScope.TEST)
  public class UnPackThemeMojo extends AbstractThemeMojo {

    /**
     * The path to the theme WAR file.
     */
    @Parameter(defaultValue = "${project.build.directory}/${project.build.finalName}.war", required = true)
    private File themeWarFile;

    /**
     * The path to the theme resources directory.
     */
    @Parameter(defaultValue = "${project.build.directory}/theme-resources", required = true)
    private File themeResourcesDirectory;

    @Override
    public void execute() throws MojoExecutionException {
      getLog().info("Unpacking theme resources from " + themeWarFile + " to " + themeResourcesDirectory);

      try {
        unpackThemeWar(themeWarFile, themeResourcesDirectory);
      } catch (IOException e) {
        throw new MojoExecutionException("Failed to unpack theme resources", e);
      }
    }

    /**
     * Unpack the theme resources from the theme WAR file.
     *
     * @param themeWarFile          the theme WAR file
     * @param themeResourcesDirectory the theme resources directory
     * @throws IOException if an error occurs while unpacking the theme resources
     */
    private void unpackThemeWar(File themeWarFile, File themeResourcesDirectory) throws IOException {
      if (!themeWarFile.exists()) {
        throw new IOException("Theme WAR file does not exist: " + themeWarFile);
      }

      if (!themeResourcesDirectory.exists()) {
        if (!themeResourcesDirectory.mkdirs()) {
          throw new IOException("Failed to create theme resources directory: " + themeResourcesDirectory);
        }
      }

      try (ArchiveInputStream ais = new ArchiveInputStream(new FileInputStream(themeWarFile))) {
        ArchiveEntry entry;
        while ((entry = ais.getNextEntry()) != null) {
          if (entry.isDirectory()) {
            continue;
          }

          File outputFile = new File(themeResourcesDirectory, entry.getName());
          if (!outputFile.getParentFile().exists()) {
            if (!outputFile.getParentFile().mkdirs()) {
              throw new IOException("Failed to create directory: " + outputFile.getParentFile());
            }
          }

          try (OutputStream os = new FileOutputStream(outputFile)) {
            IOUtils.copy(ais, os);
          }
        }
      }
    }
  }

```