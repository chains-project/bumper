```java
import org.cactoos.list.ListOf;

import java.util.List;

public class RtTransaction {

    public List<String> getTransactionList() {
        return new ListOf<>(
                "transaction1",
                "transaction2",
                "transaction3"
        );
    }
}
```