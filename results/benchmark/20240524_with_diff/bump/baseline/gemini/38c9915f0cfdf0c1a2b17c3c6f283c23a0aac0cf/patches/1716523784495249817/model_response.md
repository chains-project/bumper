```java
import org.cactoos.bytes.BytesOf;

public class WalletsIn {

    public String getWallets() {
        return new BytesOf(new JoinedText(",")).asString();
    }
}
```