```java
import org.cactoos.scalar.Solid;
import org.cactoos.text.TextOfScalar;

public class WalletsIn {

    public Solid<String> getWallets(String url) {
        return new Solid<>(new TextOfScalar(url));
    }
}
```