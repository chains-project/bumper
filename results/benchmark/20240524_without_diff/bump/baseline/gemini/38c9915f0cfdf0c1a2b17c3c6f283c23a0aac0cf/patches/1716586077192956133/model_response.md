```java
import org.cactoos.scalar.SolidScalar;

public class WalletsIn {

    public SolidScalar<String> walletIn(String walletId) {
        return new SolidScalar<>(walletId);
    }
}
```