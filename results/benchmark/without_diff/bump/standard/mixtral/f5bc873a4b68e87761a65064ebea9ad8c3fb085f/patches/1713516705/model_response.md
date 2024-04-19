Here's the proposed patch for the failing client code:
```java
import java.io.File;
import org.codehaus.plexus.components.io.filemanipulator.FileManipulator;

public class AbstractThemeMojo {
    // ...

    private FileManipulator fileManipulator;

    // ...

    @Parameter(defaultValue = "${project.build.directory}/tobago-theme-plugin/theme/")
    private File outputDirectory;

    // ...

    protected void deleteDirectory(File directory) throws MojoExecutionException {
        try {
            if (directory.exists()) {
                fileManipulator.removeAll(directory);
            }
        } catch (IOException e) {
            throw new MojoExecutionException("Error deleting directory: " + directory, e);
        }
    }

    // ...
}
```
In the provided code, I added the `FileManipulator` class from the `org.codehaus.plexus.components.io.filemanipulator` package. This class is used in the `deleteDirectory` method to remove the contents of a directory. This change should resolve the dependency issue.