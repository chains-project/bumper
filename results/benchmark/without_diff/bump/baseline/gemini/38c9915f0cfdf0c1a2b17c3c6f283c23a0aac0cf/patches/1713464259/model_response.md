```java
import org.cactoos.text.JoinedText;

public class WalletsIn {

    public String walletsIn(String url) throws Exception {
        String urlWithParams = new JoinedText(
                url,
                "?",
                "limit=",
                String.valueOf(100),
                "&",
                "offset=",
                String.valueOf(0)
        ).asString();

        return new JoinedText(
                "{\"wallets\":[",
                new ZoldClient(urlWithParams).get(),
                "]}"
        ).asString();
    }
}
```