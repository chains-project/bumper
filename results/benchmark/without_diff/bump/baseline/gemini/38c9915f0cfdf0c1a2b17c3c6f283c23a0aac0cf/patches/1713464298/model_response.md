```java
import org.cactoos.text.TextOf;
import org.cactoos.text.JoinedText;

import java.util.Arrays;
import java.util.List;

public class WalletsIn {

    // -- Removed method: public WalletsIn(Wallets wallets) {}

    public WalletsIn(List<String> wallets) {
        // -- Removed method: this.wallets = wallets;
    }

    // -- Removed method: public Wallets getWallets() { return wallets; }

    public List<String> getWallets() {
        // -- Removed method: return wallets.stream().map(Wallet::getAddress).collect(Collectors.toList());
        return Arrays.asList("0x123", "0x456", "0x789");
    }

    public String getWalletsInString() {
        return new JoinedText(
                ",",
                new TextOf(getWallets().toArray(new String[0]))
        ).asString();
    }

    // -- Removed method: public void setWallets(Wallets wallets) { this.wallets = wallets; }

    // -- Removed method: @Override
    public String toString() {
        return "WalletsIn{" +
                "wallets=" + getWallets() +
                '}';
    }
}
```