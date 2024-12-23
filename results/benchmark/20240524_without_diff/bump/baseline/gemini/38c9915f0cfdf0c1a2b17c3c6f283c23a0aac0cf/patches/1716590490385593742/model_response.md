```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class RtTransaction {

    private final URI uri;

    public RtTransaction(URI uri) {
        this.uri = uri;
    }

    public String getTransaction(String transactionId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(uri.resolve(transactionId))
                .GET()
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new RuntimeException("Error retrieving transaction: " + response.statusCode());
        }

        return new UncheckedText(response.body()).asString();
    }
}
```