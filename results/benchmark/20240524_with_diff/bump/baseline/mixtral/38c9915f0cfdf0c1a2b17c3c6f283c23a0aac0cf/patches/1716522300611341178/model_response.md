Here's a possible patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoCheckedBytes;
import org.cactoos.io.InputOf;
import org.cactoos.text.TextOf;
import org.cactoos.text.Joined;
import java.io.IOException;

public class RtTransaction {
  // ...
  private Scalar<String> readFile(final String path) throws IOException {
    return new IoCheckedBytes(new InputOf(path)).asBytes();
  }

  private String readFileAsString(final String path) throws IOException {
    return new TextOf(readFile(path)).asString();
  }

  private Joined<String> readFilesAsString(final String... paths) throws IOException {
    final Scalar<Iterable<String>> files = new ScalarOf(() -> {
      try {
        final Iterable<String> result = new Iterable<String>() {
          @Override
          public Iterator<String> iterator() {
            return new Iterator<String>() {
              private int index = 0;

              @Override
              public boolean hasNext() {
                return index < paths.length;
              }

              @Override
              public String next() {
                try {
                  return readFileAsString(paths[index++]);
                } catch (final IOException e) {
                  throw new UncheckedIOException(e);
                }
              }
            };
          }
        };
        return result;
      } catch (final IOException e) {
        throw new UncheckedIOException(e);
      }
    });
    return new Joined<>("", files.value());
  }
  // ...
}
```

The changes made are:

* Replace `IoCheckedScalar` with `IoCheckedBytes` and `TextOf` to read the file content as bytes and then convert it to a string.
* Replace `IterableEnvelope` with a custom implementation using `ScalarOf` and `Iterable` to read multiple files and join their content.
* Add `UncheckedIOException` to handle exceptions in `readFilesAsString` method.
* Add import statements for new classes.
* Remove unused import statement for `IoCheckedScalar`.