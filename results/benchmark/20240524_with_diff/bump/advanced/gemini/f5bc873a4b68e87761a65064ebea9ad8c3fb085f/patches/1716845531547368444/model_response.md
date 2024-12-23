```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.artifact.Artifact;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugins.annotations.LifecyclePhase;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.plugins.annotations.ResolutionScope;
import org.apache.maven.project.MavenProjectHelper;
import org.apache.maven.shared.artifact.filter.collection.ArtifactsFilter;
import org.apache.maven.shared.artifact.filter.collection.FilterArtifacts;
import org.apache.maven.shared.utils.StringUtils;
import org.apache.maven.shared.utils.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Copies the resources from the source directory to the output directory.
 *
 * @author <a href="mailto:nicolas.deloof@gmail.com">Nicolas De Loof</a>
 * @since 1.0.0
 */
@Mojo(name = "copy-resources", defaultPhase = LifecyclePhase.PROCESS_RESOURCES, requiresDependencyResolution = ResolutionScope.COMPILE)
public class CopyResourcesMojo extends AbstractThemeMojo {

  /**
   * The source directory containing the resources to be copied.
   */
  @Parameter(defaultValue = "${project.basedir}/src/main/resources", required = true)
  private File sourceDirectory;

  /**
   * The output directory where the resources will be copied.
   */
  @Parameter(defaultValue = "${project.build.outputDirectory}", required = true)
  private File outputDirectory;

  /**
   * The list of resources that should be copied.
   */
  @Parameter
  private List<String> includes;

  /**
   * The list of resources that should not be copied.
   */
  @Parameter
  private List<String> excludes;

  /**
   * Whether to overwrite existing files.
   */
  @Parameter(defaultValue = "false")
  private boolean overwrite;

  /**
   * Whether to skip the execution.
   */
  @Parameter(defaultValue = "false")
  private boolean skip;

  /**
   * Whether to include the default resources of the parent theme.
   */
  @Parameter(defaultValue = "false")
  private boolean includeParentResources;

  /**
   * The project helper.
   */
  @Component
  private MavenProjectHelper projectHelper;

  /**
   * The artifact filter.
   */
  @Component
  private FilterArtifacts filterArtifacts;

  /**
   * Executes the mojo.
   *
   * @throws MojoExecutionException if an error occurs
   */
  @Override
  public void execute() throws MojoExecutionException {
    if (skip) {
      getLog().info("Skipping execution.");
      return;
    }

    if (sourceDirectory == null || !sourceDirectory.exists()) {
      throw new MojoExecutionException("Source directory '" + sourceDirectory + "' does not exist.");
    }

    if (outputDirectory == null) {
      throw new MojoExecutionException("Output directory is null.");
    }

    if (!outputDirectory.exists()) {
      if (!outputDirectory.mkdirs()) {
        throw new MojoExecutionException("Failed to create output directory '" + outputDirectory + "'.");
      }
    }

    List<String> includesList = includes == null ? Collections.emptyList() : includes;
    List<String> excludesList = excludes == null ? Collections.emptyList() : excludes;

    if (includeParentResources) {
      MavenProject parentProject = project.getParent();
      if (parentProject != null) {
        Set<Artifact> parentArtifacts = parentProject.getArtifacts();
        for (Artifact parentArtifact : parentArtifacts) {
          if (parentArtifact.getType().equals("war")) {
            File parentWarFile = parentArtifact.getFile();
            if (parentWarFile.exists()) {
              try {
                File parentResourcesDirectory = new File(parentWarFile, "WEB-INF/classes");
                if (parentResourcesDirectory.exists()) {
                  FileUtils.copyDirectoryStructure(parentResourcesDirectory, outputDirectory);
                }
              } catch (IOException e) {
                throw new MojoExecutionException("Failed to copy resources from parent theme.", e);
              }
            }
          }
        }
      }
    }

    try {
      Set<File> filesToCopy = filterArtifacts.filter(
          sourceDirectory,
          includesList,
          excludesList,
          new ArtifactsFilter() {
            @Override
            public boolean include(Artifact artifact) {
              return false;
            }
          });

      for (File fileToCopy : filesToCopy) {
        String relativePath = fileToCopy.getPath().substring(sourceDirectory.getPath().length() + 1);
        File targetFile = new File(outputDirectory, relativePath);
        if (overwrite || !targetFile.exists()) {
          FileUtils.copyFile(fileToCopy, targetFile);
          getLog().debug("Copied resource '" + relativePath + "'.");
        } else {
          getLog().debug("Skipping existing resource '" + relativePath + "'.");
        }
      }
    } catch (IOException e) {
      throw new MojoExecutionException("Failed to copy resources.", e);
    }
  }
}
```