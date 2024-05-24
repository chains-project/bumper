```java
import org.cactoos.text.JoinedText;

import java.util.List;

public class WalletsIn {

    public List<Wallet> wallets(String address) {
        return new JoinedText(
                "https://",
                address,
                "/api/v1/wallets"
        ).toString();
    }
}
```