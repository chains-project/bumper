```java
import org.cactoos.text.UncheckedText;

import java.io.IOException;

public class WalletsIn {


    public static String walletsIn(String uri, String walletId) throws IOException {
        String requestBody = new UncheckedText("{\"wallet_id\": \"" + walletId + "\"}").asString();
        return new UncheckedText(new HttpRequest(uri + "/wallets/" + walletId, requestBody).send()).asString();
    }
}
```