```java
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class WalletsIn {

    public List<Wallet> walletsIn(Path path) throws IOException {
        List<Wallet> wallets = new ArrayList<>();
        Files.list(path).forEach(walletPath -> {
            try {
                wallets.add(new IoCheckedScalar<>(walletPath::toFile, Wallet::fromFile).value());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
        return wallets;
    }
}
```