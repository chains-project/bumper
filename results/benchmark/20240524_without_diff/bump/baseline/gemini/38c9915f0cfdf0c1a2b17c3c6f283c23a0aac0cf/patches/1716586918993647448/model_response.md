```java
import org.cactoos.scalar.UncheckedScalar;
import org.cactoos.text.UncheckedText;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class RtTransaction {

    public static UncheckedScalar<Integer> sendTransaction(String transaction) throws IOException {
        URL url = new URL("https://api.zold.io/api/v1/transactions");

        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/json");
        connection.setRequestProperty("Accept", "application/json");
        connection.setDoOutput(true);

        UncheckedText.of(transaction).stream().writeTo(connection.getOutputStream());

        if (connection.getResponseCode() != 200) {
            throw new IOException("Error sending transaction: " + connection.getResponseMessage());
        }

        return new UncheckedScalar<>(connection.getInputStream());
    }

}
```