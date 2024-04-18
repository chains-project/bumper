```java
import org.cactoos.text.JoinedText;

public class WalletsIn {

    public WalletsIn(Wallets wallets) {
        this.wallets = wallets;
    }

    public String print() {
        String result = new JoinedText(
                System.lineSeparator(),
                wallets.stream().map(Wallet::toString).iterator()
        ).toString();
        return result;
    }

    private final Wallets wallets;
}
```