```java
import org.cactoos.text.TextOf;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.List;
import java.util.stream.Collectors;

public class WalletsIn {

    public List<String> getWallets(String url) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        String[] wallets = new TextOf(response.body()).toString().split(",");
        return List.of(wallets).stream().map(String::trim).collect(Collectors.toList());
    }
}
```