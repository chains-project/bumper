```java
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class WalletsIn extends IoCheckedScalar<String> {

    private final Path path;

    public WalletsIn(Path path) {
        this.path = path;
    }

    @Override
    public String value() throws IOException {
        return Files.readString(path);
    }
}
```