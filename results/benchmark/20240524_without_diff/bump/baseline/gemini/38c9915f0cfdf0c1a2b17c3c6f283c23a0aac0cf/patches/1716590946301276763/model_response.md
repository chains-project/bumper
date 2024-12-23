```java
import org.cactoos.scalar.IoCheckedScalar;
import org.cactoos.text.UncheckedText;
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

public class RtTransaction {

    private final String url;
    private final String body;

    public RtTransaction(String url, String body) {
        this.url = url;
        this.body = body;
    }

    public String execute() throws IOException {
        try (InputStream inputStream = new UncheckedText(new TextOf(this.body)).stream().collect(Collectors.joining()).getBytes(StandardCharsets.UTF_8)) {
            return new IoCheckedScalar<>(
                    () -> new InputStreamReader(inputStream, StandardCharsets.UTF_8)
            ).value();
        }
    }
}
```