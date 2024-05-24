```java
import org.cactoos.bytes.BytesOf;

public class WalletsIn {

    public byte[] wallets(String url) {
        return new BytesOf(new UncheckedText(url)).asBytes();
    }
}
```