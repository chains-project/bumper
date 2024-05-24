```java
import org.cactoos.bytes.BytesOf;

public class WalletsIn {

    public String getWalletsIn(String walletsIn) {
        return new BytesOf(new JoinedText(walletsIn, ",")).asString();
    }
}
```