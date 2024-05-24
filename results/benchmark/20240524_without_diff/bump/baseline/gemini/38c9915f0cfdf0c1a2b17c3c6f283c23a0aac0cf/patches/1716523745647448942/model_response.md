```java
import org.cactoos.bytes.BytesOf;

public class WalletsIn {

    public BytesOf getWalletsIn(String url) {
        return new BytesOf(new JoinedText(url, "/wallets/in"));
    }

}
```