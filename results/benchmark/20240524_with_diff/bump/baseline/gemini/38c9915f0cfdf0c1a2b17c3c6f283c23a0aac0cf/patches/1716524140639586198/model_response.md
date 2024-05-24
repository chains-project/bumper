```java
import org.cactoos.text.JoinedText;

import java.util.List;

public class WalletsIn {

    public String getWallets(List<String> addresses) {
        return new JoinedText(
                ",",
                addresses
        ).asString();
    }
}
```