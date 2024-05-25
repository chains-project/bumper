```java
import org.cactoos.text.UncheckedText;
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Optional;

public class RtTransaction {

    // ...

    private static String getTransactionHash(String txHash) throws IOException {
        String url = "https://api.zold.io/v1/transactions/" + txHash;
        Optional<String> response = Optional.empty();

        try (InputStream is = new URL(url).openStream();
             Reader reader = new InputStreamReader(is, StandardCharsets.UTF_8)) {
            response = Optional.of(new UncheckedText(new TextOf(reader)).asString());
        }

        return response.orElseThrow(() -> new RuntimeException("Transaction not found"));
    }

    // ...

}
```