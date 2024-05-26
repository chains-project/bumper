Here is the modified code that should fix the error:

```java
import java.io.File;
import java.nio.file.Paths;

// ...

File file = new File("path/to/your/file");

// Use NIO.2 to get the parent
File parent = Paths.get(file.getAbsolutePath()).toFile().getParentFile();
```

This code snippet uses the `java.nio.file.Paths` class to get the parent directory of the given file, instead of relying on the deprecated `File` class. The `Path` class provides a more robust and efficient way to manipulate and query file and directory paths.
`Path parent = Paths.get(file.getAbsolutePath()).toFile().getParentFile();` can be replaced with `parent = file.toPath().getParent().toFile();` in Java 8 and above.