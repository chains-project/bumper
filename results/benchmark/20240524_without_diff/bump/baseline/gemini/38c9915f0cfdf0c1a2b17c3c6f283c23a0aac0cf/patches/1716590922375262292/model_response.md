```java
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;

public class RtTransaction {

    // ...

    public IoCheckedScalar<String> getTransactionData() throws IOException {
        return new IoCheckedScalar<>(
                () -> "transaction_data",
                IOException::new
        );
    }

    // ...
}
```