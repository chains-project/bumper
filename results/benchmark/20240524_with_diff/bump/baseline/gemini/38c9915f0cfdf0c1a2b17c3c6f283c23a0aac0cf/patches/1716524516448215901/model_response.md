```java
import org.cactoos.text.FormattedText;

public class WalletsIn {

    public WalletsIn(Wallets wallets) {
        wallets.stream().forEach(wallet -> {
            new FormattedText("%s: %s", wallet.name(), wallet.address()).print();
        });
    }
}
```