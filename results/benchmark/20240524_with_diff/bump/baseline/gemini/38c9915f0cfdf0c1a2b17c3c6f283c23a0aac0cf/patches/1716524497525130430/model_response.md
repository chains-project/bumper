```java
import org.cactoos.text.FormattedText;
import org.cactoos.text.UncheckedText;

public class WalletsIn {

    public String walletsIn(String url, String token, String walletId) {
        String response = new UncheckedText(
                new FormattedText(
                        "GET %s/wallets/%s HTTP/1.1\r\n" +
                                "Authorization: Bearer %s\r\n" +
                                "\r\n",
                        url,
                        walletId,
                        token
                )
        ).asString();
        return response;
    }
}
```