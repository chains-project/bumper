```java
import org.cactoos.scalar.Scalar;
import org.cactoos.scalar.Unchecked;

import java.util.function.Function;

public class WalletsIn {

    // ...

    public Scalar<String> getWallets(Function<String, String> function) {
        return new Unchecked<>(() -> function.apply("wallets"));
    }

    // ...
}
```