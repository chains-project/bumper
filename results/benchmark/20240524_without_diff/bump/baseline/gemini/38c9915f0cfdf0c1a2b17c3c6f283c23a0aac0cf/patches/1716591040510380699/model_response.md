```java
import org.cactoos.scalar.IoCheckedScalar;

import java.io.File;
import java.io.IOException;

public class RtTransaction {

    public RtTransaction(File file) {
        this.file = file;
    }

    public IoCheckedScalar<String> getReceipt() throws IOException {
        return new IoCheckedScalar<>(() -> file.exists() ? "receipt" : null);
    }

    private final File file;
}
```