```java
import org.cactoos.text.Joined;

import java.util.Arrays;

public class WalletsIn {

    public static String walletsIn(String... wallets) {
        return new Joined(";", Arrays.stream(wallets)).asString();
    }
}
```