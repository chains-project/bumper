```java
import org.cactoos.text.FormattedText;

import java.util.List;

public class WalletsIn {
    public String execute(List<String> wallets) {
        String walletsFormatted = new FormattedText(
                "Wallets:\n%s",
                String.join("\n", wallets)
        ).asString();

        return walletsFormatted;
    }
}
```