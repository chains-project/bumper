```java
import org.cactoos.text.JoinedText;

public class WalletsIn {

    public String walletsIn(String address) {
        return new JoinedText(
                "{\"jsonrpc\":\"2.0\",\"method\":\"zold_walletsIn\",\"params\":[",
                "\"", address, "\""
                ],
                ",\"id\":1}").asString();
    }
}
```