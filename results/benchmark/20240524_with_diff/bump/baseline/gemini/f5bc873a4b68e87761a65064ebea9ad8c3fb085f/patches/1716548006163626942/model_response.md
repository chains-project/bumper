```java
import org.apache.maven.artifact.DependencyResolutionRequiredException;

public class UnPackThemeMojo extends AbstractMojo {

    /**
     * Create a new instance of this mojo.
     */
    public UnPackThemeMojo() {
    }

    /**
     * Execute the mojo.
     *
     * @throws MojoExecutionException if an error occurs.
     */
    public void execute() throws MojoExecutionException {
        try {
            getLog().info("Unpacking theme " + themeName + " from " + themePath + " to " + targetPath);
            unpackTheme();
        } catch (DependencyResolutionRequiredException e) {
            throw new MojoExecutionException("Failed to unpack theme", e);
        }
    }

    /**
     * Unpack the theme.
     *
     * @throws DependencyResolutionRequiredException if an error occurs.
     */
    private void unpackTheme() throws DependencyResolutionRequiredException {
        // Get the theme file.
        final File themeFile = new File(themePath);

        // Create the target directory.
        final File targetDir = new File(targetPath);
        targetDir.mkdirs();

        // Unpack the theme file.
        try (final ZipFile zipFile = new ZipFile(themeFile)) {
            for (final ZipEntry entry : Collections.list(zipFile.entries())) {
                if (!entry.isDirectory()) {
                    final File targetFile = new File(targetDir, entry.getName());
                    targetFile.getParentFile().mkdirs();
                    try (final InputStream inputStream = zipFile.getInputStream(entry)) {
                        try (final FileOutputStream outputStream = new FileOutputStream(targetFile)) {
                            IOUtils.copy(inputStream, outputStream);
                        }
                    }
                }
            }
        } catch (IOException e) {
            throw new MojoExecutionException("Failed to unpack theme", e);
        }
    }
}
```