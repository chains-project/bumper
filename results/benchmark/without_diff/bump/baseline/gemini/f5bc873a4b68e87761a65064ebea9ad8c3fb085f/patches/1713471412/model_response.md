```java
import org.apache.maven.artifact.DependencyResolutionRequiredException;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class UnPackThemeMojo extends AbstractThemeMojo {

  @Parameter(defaultValue = "${project.build.directory}", required = true)
  private File outputDirectory;

  @Parameter(defaultValue = "${project.build.directory}", required = true)
  private File targetDirectory;

  @Parameter(defaultValue = "${project.build.directory}", required = true)
  private File unpackDirectory;

  @Override
  public void execute() throws MojoExecutionException, DependencyResolutionRequiredException {
    try {
      // Get the theme file
      File themeFile = getThemeFile();

      // Create the output directory
      if (!outputDirectory.exists()) {
        outputDirectory.mkdirs();
      }

      // Create the target directory
      if (!targetDirectory.exists()) {
        targetDirectory.mkdirs();
      }

      // Create the unpack directory
      if (!unpackDirectory.exists()) {
        unpackDirectory.mkdirs();
      }

      // Unpack the theme file
      unzip(themeFile, unpackDirectory);

      // Copy the theme resources to the output directory
      copyResources(unpackDirectory, outputDirectory);

      // Copy the theme resources to the target directory
      copyResources(unpackDirectory, targetDirectory);

      // Remove the unpack directory
      deleteDirectory(unpackDirectory);

    } catch (IOException e) {
      throw new MojoExecutionException("Error unpacking theme file", e);
    }
  }

  private void copyResources(File sourceDirectory, File targetDirectory) throws IOException {
    List<Path> files = Files.walk(sourceDirectory.toPath())
        .filter(Files::isRegularFile)
        .collect(Collectors.toList());

    for (Path file : files) {
      Path relativePath = sourceDirectory.toPath().relativize(file);
      Path targetFile = Paths.get(targetDirectory.getAbsolutePath(), relativePath.toString());
      Files.copy(file, targetFile);
    }
  }

  private void deleteDirectory(File directory) throws IOException {
    Files.walk(directory.toPath())
        .sorted(Comparator.reverseOrder())
        .map(Path::toFile)
        .forEach(File::delete);
  }
}
```