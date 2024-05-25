```java
import org.cactoos.text.JoinedText;

import java.util.List;

public class WalletsIn {

    public String getWallets(String url, String accessToken) {
        List<String> walletIds = List.of("wallet1", "wallet2");
        return new JoinedText(
                System.lineSeparator(),
                walletIds
        ).asString();
    }
}
```