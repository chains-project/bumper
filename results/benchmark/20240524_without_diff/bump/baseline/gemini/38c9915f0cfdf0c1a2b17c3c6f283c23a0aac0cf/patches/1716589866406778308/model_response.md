```java
import org.cactoos.list.ListOf;

import java.util.List;

public class RtTransaction {

    public List<String> getTransactions(String address) {
        return new ListOf<>(address);
    }
}
```