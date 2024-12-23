```java
import org.cactoos.text.UncheckedText;
import org.cactoos.text.TextOf;

import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class RtTransaction {
    // ...

    private String getTransactionDetails(String transactionId) {
        String url = String.format("https://api.zold.io/v1/transactions/%s", transactionId);
        String encodedCredentials = Base64.getEncoder().encodeToString(
                (this.apiKey + ":" + this.apiSecret).getBytes(StandardCharsets.UTF_8));

        String response = new UncheckedText(
                () -> new TextOf(
                        new RtHttpClient(url, encodedCredentials).send()
                )
        ).asString();

        return response;
    }

    // ...
}
```