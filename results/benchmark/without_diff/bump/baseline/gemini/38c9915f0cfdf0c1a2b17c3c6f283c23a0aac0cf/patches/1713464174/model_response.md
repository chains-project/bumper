```java
import org.cactoos.text.JoinedText;
import org.cactoos.text.TextOf;

import java.util.List;

public class WalletsIn {

    public String getWalletsIn(String userId, List<String> walletIds) {
        return new JoinedText(
                "\n",
                new TextOf("## Wallets in"),
                new TextOf("**User ID:** " + userId),
                new TextOf("**Wallet IDs:** " + String.join(", ", walletIds))
        ).asString();
    }
}
```