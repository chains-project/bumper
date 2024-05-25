```java
import org.cactoos.text.JoinedText;

import java.util.ArrayList;
import java.util.List;

public class WalletsIn {

    public String walletsIn(String body) {
        List<String> lines = new ArrayList<>();
        lines.add(body);
        return new JoinedText("\n", lines).asString();
    }
}
```