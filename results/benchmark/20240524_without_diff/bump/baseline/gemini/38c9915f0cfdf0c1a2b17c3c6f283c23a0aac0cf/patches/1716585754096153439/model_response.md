```java
import org.cactoos.text.JoinedText;

import java.util.List;
import java.util.stream.Collectors;

public class WalletsIn {

    public List<String> getWallets() {
        return List.of("wallet1", "wallet2", "wallet3");
    }

    public String getWalletsInString() {
        return new JoinedText(", ", getWallets()).asString();
    }
}
```