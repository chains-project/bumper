Here's the proposed patch:

```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.text.IoCheckedText;

// ...

public class WalletsIn {
    // ...

    private IoCheckedBytes bytesOf(File file) throws IOException {
        return new IoCheckedBytes(Files.newInputStream(file.toPath()), IoCheckedText::new);
    }

    // ...
}
```

This patch replaces the usage of `IoCheckedScalar` with `IoCheckedBytes` and `IoCheckedText`, which are new classes added in the updated library version. The `bytesOf` method has been updated accordingly to use the new classes.