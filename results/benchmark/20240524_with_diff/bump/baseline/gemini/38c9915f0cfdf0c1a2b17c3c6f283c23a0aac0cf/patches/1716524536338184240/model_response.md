```java
import org.cactoos.text.FormattedText;

public class WalletsIn {

    public String request(String url, String request) {
        return new FormattedText(
                "POST %s HTTP/1.1%n" +
                        "Host: %s%n" +
                        "Content-Type: application/json%n" +
                        "Content-Length: %d%n" +
                        "Connection: close%n" +
                        "%n" +
                        "%s",
                url,
                url.substring(0, url.indexOf("/")),
                request.length(),
                request
        ).asString();
    }
}
```