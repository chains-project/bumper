```java
import org.cactoos.list.ListOf;
import org.cactoos.map.MapEntry;
import org.cactoos.map.MapOf;
import org.cactoos.set.SetOf;
import org.cactoos.scalar.SolidScalar;
import org.cactoos.text.TextOf;

import java.util.Map;
import java.util.Set;

public class WalletsIn {

    private final Wallets wallets;
    private final Set<String> walletIds;

    public WalletsIn(Wallets wallets, Set<String> walletIds) {
        this.wallets = wallets;
        this.walletIds = walletIds;
    }

    public Map<String, Wallet> perform() {
        return new MapOf<>(
                new ListOf<>(walletIds).stream().map(
                        walletId -> new MapEntry<>(walletId, wallets.get(walletId))
                )
        );
    }
}
```