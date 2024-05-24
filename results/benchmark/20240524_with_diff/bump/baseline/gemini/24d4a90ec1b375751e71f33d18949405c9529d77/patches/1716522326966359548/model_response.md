```java
import com.jcabi.aspects.Tv;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class BucketRule {

    private final Path root;

    public BucketRule(Path root) {
        this.root = root;
    }

    public List<String> list() throws IOException {
        return Files.walk(this.root)
                .filter(Files::isRegularFile)
                .map(Path::getFileName)
                .map(Path::toString)
                .collect(Collectors.toList());
    }

    public Tv tv() {
        return new Tv();
    }
}
```