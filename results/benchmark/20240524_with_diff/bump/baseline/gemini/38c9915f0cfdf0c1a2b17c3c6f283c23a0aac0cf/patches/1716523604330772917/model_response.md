```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.io.CheckedBytes;

public class WalletsIn {
    // ...
    public void getWallets(String url, String apiKey) {
        // ...
        byte[] data = new IoCheckedBytes(new CheckedBytes(response.body(), this::validateResponse)).asBytes();
        // ...
    }
    // ...
}
```