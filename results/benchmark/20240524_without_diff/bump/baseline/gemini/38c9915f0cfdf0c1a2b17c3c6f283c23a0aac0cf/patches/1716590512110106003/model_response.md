```java
import org.cactoos.text.TextOf;

import java.util.List;

public class RtTransaction {

    private final List<RtTransactionItem> items;

    public RtTransaction(List<RtTransactionItem> items) {
        this.items = items;
    }

    public String toText() {
        return new TextOf(items).asString();
    }
}
```