```java
import org.cactoos.text.FormattedText;

public class WalletsIn {

    // ...

    @Override
    public String walletsIn(String address) throws Exception {
        return new FormattedText(
                "GET /api/v1/wallets/%s/in?limit=%d&offset=%d",
                address,
                limit,
                offset
        ).asString();
    }

    // ...

}
```