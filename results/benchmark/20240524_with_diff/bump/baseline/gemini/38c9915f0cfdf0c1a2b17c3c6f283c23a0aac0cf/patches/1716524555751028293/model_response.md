```java
import org.cactoos.text.FormattedText;

public class WalletsIn {

    public String walletsIn(String address) {
        return new FormattedText(
                "GET /v1/wallets/%s/in", address
        ).asString();
    }
}
```