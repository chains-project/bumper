Here's the patched version of the failing method:
```java
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

// ...

private void checkDirectory(File directory) throws MojoFailureException {
    Path path = Paths.get(directory.getPath());
    if (!Files.exists(path)) {
        try {
            Files.createDirectory(path);
        } catch (Exception e) {
            throw new MojoFailureException("Cannot create directory " + directory.getPath(), e);
        }
    } else if (!Files.isDirectory(path)) {
        throw new MojoFailureException(directory.getPath() + " exists but is not a directory");
    }
}
```
Changes made:

* Imported new classes from the Java NIO package to replace the deprecated `File` class methods.
* Replaced `File.getPath()` with `Paths.get(directory.getPath())` to convert the `File` object to a `Path` object.
* Replaced `File.exists()` and `File.isDirectory()` with `Files.exists()` and `Files.isDirectory()` to check for file existence and directory validity.
* Replaced `File.createDirectory()` with `Files.createDirectory()` to create the directory.