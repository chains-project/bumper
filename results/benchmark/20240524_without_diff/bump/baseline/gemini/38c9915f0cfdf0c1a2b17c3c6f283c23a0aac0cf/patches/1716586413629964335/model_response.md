```java
import org.cactoos.iterable.IterableOf;
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class WalletsIn {

    private final Client client;
    private final String network;

    public WalletsIn(Client client, String network) {
        this.client = client;
        this.network = network;
    }

    public List<Wallet> getWallets() throws IOException {
        List<Wallet> wallets = new ArrayList<>();
        for (String walletId : new IoCheckedScalar<>(() -> client.getWallets(network)).value()) {
            wallets.add(new Wallet(client, network, walletId));
        }
        return wallets;
    }
}
```