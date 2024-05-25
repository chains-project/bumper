```java
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;
import java.io.InputStream;

public class WalletsIn {

    private final IoCheckedScalar<InputStream> input;

    public WalletsIn(IoCheckedScalar<InputStream> input) {
        this.input = input;
    }

    public String wallets() throws IOException {
        String wallets = "";
        try (InputStream inputStream = input.value()) {
            wallets = new String(inputStream.readAllBytes());
        }
        return wallets;
    }
}
```