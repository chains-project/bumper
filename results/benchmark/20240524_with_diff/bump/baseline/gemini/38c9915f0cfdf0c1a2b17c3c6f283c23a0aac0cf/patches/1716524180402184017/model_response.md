```java
import org.cactoos.text.JoinedText;
import java.util.List;

public class WalletsIn {

    public static String walletsIn(String url, String token, List<String> walletIds) {
        return new JoinedText(
                "GET ",
                url,
                "/wallets?ids=",
                String.join(",", walletIds),
                " HTTP/1.1\r\n",
                "Authorization: Bearer ",
                token,
                "\r\n\r\n"
        ).asString();
    }
}
```