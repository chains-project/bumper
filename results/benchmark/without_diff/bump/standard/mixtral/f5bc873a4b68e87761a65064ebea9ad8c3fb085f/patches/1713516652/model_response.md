Here's the patched version of the failing method:
```java
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

// ...

private void copyResourceBundle(File targetDir, String sourcePath) throws IOException {
    Path source = Paths.get(sourcePath);
    String fileName = source.getFileName().toString();
    Path target = Paths.get(targetDir.getPath(), fileName);
    Files.copy(source, target);
}
```
Changes made:

* Imported the missing classes from `java.nio.file` package.
* Replaced `File` operations with `Path` operations.
* Changed the method signature to include `IOException`.

These changes make the code more robust and avoid the usage of the removed library method.