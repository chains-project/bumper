```java
import org.cactoos.text.FormattedText;

public class WalletsIn {

    // ...

    public String getWalletsIn() {
        return new FormattedText(
                "GET /api/v1/wallets?status=%s",
                this.status
        ).asString();
    }

    // ...
}
```