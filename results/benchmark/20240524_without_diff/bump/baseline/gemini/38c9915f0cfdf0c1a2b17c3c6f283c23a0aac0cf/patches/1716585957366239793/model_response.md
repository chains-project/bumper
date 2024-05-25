```java
import org.cactoos.text.JoinedText;
import org.cactoos.text.TextOf;

import java.util.List;

public class WalletsIn {

    /**
     * @param wallets the wallets
     * @return the text
     */
    public TextOf walletsIn(List<String> wallets) {
        return new JoinedText(
                "Wallet addresses:\n",
                new JoinedText(wallets, "\n")
        );
    }
}
```