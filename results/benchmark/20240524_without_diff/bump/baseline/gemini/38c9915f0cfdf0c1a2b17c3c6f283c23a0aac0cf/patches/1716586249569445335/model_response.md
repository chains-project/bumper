```java
  import org.cactoos.scalar.IoCheckedScalar;
  import java.io.File;
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.nio.file.Paths;
  import java.util.stream.Stream;

  public class WalletsIn {

    public WalletsIn(final String path) throws IOException {
      try (Stream<Path> files = Files.walk(Paths.get(path))) {
        files
            .filter(Files::isRegularFile)
            .forEach(file -> {
              try {
                final String content = new String(Files.readAllBytes(file));
                // Do something with the content of the file
              } catch (IOException e) {
                throw new RuntimeException(e);
              }
            });
      }
    }
  }
```