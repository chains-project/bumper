```java
import org.cactoos.scalar.SolidScalar;

public class WalletsIn {

    public static SolidScalar<String> of(String... wallets) {
        return new SolidScalar<>(String.join(",", wallets));
    }
}
```