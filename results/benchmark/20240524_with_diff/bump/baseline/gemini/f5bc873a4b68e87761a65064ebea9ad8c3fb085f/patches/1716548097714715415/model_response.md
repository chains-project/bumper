```java
import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.resolver.ArtifactNotFoundException;
import org.apache.maven.artifact.resolver.ArtifactResolutionException;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.artifact.ProjectArtifactMetadata;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

/**
 * Unpack the theme resources.
 */
@Mojo(name = "unpack-theme")
public class UnPackThemeMojo extends AbstractThemeMojo {

    /**
     * The theme artifact.
     */
    @Parameter(defaultValue = "${project.artifact}", required = true, readonly = true)
    private Artifact themeArtifact;

    /**
     * The theme artifact metadata.
     */
    @Parameter(defaultValue = "${project.artifactMetadata}", required = true, readonly = true)
    private ProjectArtifactMetadata themeArtifactMetadata;

    /**
     * The list of themes to unpack.
     */
    @Parameter(required = true)
    private List<Theme> themes;

    /**
     * The directory where the themes should be unpacked.
     */
    @Parameter(defaultValue = "${project.build.directory}/tobago-theme", required = true)
    private File themeDirectory;

    @Override
    public void execute() throws MojoExecutionException {
        try {
            final Set<Artifact> artifacts = themeArtifactMetadata.getArtifacts();
            for (final Theme theme : themes) {
                final String themeName = theme.getName();
                final String themeVersion = theme.getVersion();
                final Artifact themeArtifact = artifacts.stream()
                        .filter(artifact -> artifact.getArtifactId().equals(themeName) && artifact.getVersion().equals(themeVersion))
                        .findFirst()
                        .orElseThrow(() -> new MojoExecutionException("Theme '" + themeName + "' with version '" + themeVersion + "' not found in project dependencies."));
                final Path themePath = Paths.get(themeDirectory.getAbsolutePath(), themeName, themeVersion);
                if (!Files.exists(themePath)) {
                    Files.createDirectories(themePath);
                    getLog().info("Unpacking theme '" + themeName + "' with version '" + themeVersion + "' to '" + themePath + "'.");
                    projectHelper.attachArtifact(project, themeArtifact, "zip");
                    projectHelper.unpack(themeArtifact.getFile(), themePath);
                } else {
                    getLog().info("Theme '" + themeName + "' with version '" + themeVersion + "' already unpacked to '" + themePath + "'.");
                }
            }
        } catch (final ArtifactNotFoundException | ArtifactResolutionException e) {
            throw new MojoExecutionException("Error resolving theme artifact.", e);
        } catch (final IOException e) {
            throw new MojoExecutionException("Error unpacking theme.", e);
        }
    }
}
```