```java
import org.cactoos.scalar.Solid;
import org.cactoos.text.TextOfScalar;

import java.util.Collections;

public class WalletsIn {

    public WalletsIn() {
        // Do nothing.
    }

    public String getWallets(String address) {
        Solid<String> wallets = new Solid<>(new TextOfScalar(address));
        return wallets.value();
    }
}
```