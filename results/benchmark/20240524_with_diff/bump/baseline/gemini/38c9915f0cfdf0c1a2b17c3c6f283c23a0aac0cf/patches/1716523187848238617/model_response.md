```java
import org.cactoos.text.Joined;

public class WalletsIn {

    public String getWallets(String... wallets) {
        return new Joined(wallets).asString();
    }

}
```