```java
import org.cactoos.text.JoinedText;
import org.cactoos.text.TextOf;

import java.io.IOException;
import java.util.List;

public class WalletsIn {

    public List<Wallet> walletsIn(String address) throws IOException {
        String url = String.format("https://api.zold.io/v1/wallets/in/%s", address);
        String response = new TextOf(new JoinedText(
                "GET",
                " ",
                url,
                " HTTP/1.1",
                System.lineSeparator(),
                "Host: api.zold.io",
                System.lineSeparator(),
                "Accept: application/json",
                System.lineSeparator(),
                System.lineSeparator()
        )).asString();

        return new JsonParser(response).wallets();
    }
}
```