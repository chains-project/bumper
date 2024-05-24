```java
import org.cactoos.bytes.BytesOf;

import java.nio.charset.StandardCharsets;

public class WalletsIn {
    public WalletsIn() {
        // Use BytesOf to convert the text to bytes
        BytesOf bytesOf = new BytesOf(new JoinedText("wallet1", "wallet2"), StandardCharsets.UTF_8);

        // Use the bytes in your code
        // ...
    }
}
```