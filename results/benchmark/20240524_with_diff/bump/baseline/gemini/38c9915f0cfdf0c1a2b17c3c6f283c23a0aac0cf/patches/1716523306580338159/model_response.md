```java
import org.cactoos.scalar.Solid;

public class WalletsIn {
    public Solid<String> walletsIn(String address) {
        return new Solid<>(address);
    }
}
```