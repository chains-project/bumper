Here's a fixed version of the client code:
```java
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

// ...

File file = new File("path/to/file");
try {
    // Use NIO.2 to read the file
    String content = new String(Files.readAllBytes(Paths.get(file.getPath())));
    // ...
} catch (IOException e) {
    // Handle exception
}
```
The issue was caused by using the `File` class to read the file content, which is not recommended in modern Java versions. Instead, the `Files` class from the `java.nio.file` package should be used.