```java
import org.cactoos.iterable.IterableOf;
import org.cactoos.list.ListOf;
import org.cactoos.scalar.ItemAt;

import java.util.List;

public class RtTransaction {
    public List<String> getRtTransaction(String transactionId) {
        // ...
        return new ListOf<>(new ItemAt<>(0, rtTransaction));
    }
}
```