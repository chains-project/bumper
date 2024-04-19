Here's a fixed version of the client code:
```java
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

// ...

File file = new File("path/to/file");
try {
    byte[] bytes = Files.readAllBytes(Paths.get(file.getAbsolutePath()));
    // ... use bytes ...
} catch (IOException e) {
    // handle exception ...
}
```
The failure is caused by the deprecated `File.readFileToByteArray()` method. Instead, we use `Files.readAllBytes()` from the `java.nio.file` package.