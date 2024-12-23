```java
import org.cactoos.scalar.UncheckedScalar;

import java.util.Map;

public class RtTransaction {

    // ... other fields and methods ...

    /**
     * @param transactionId transaction id
     * @param params        transaction parameters
     * @return transaction result
     */
    public Map<String, Object> execute(String transactionId, Map<String, Object> params) {
        return new UncheckedScalar<Map<String, Object>>(
                () -> getTransactionExecutor().execute(transactionId, params)
        ).value();
    }

    // ... other methods ...
}
```