```java
import org.cactoos.scalar.IoCheckedScalar;
import org.cactoos.scalar.UncheckedScalar;

import java.io.IOException;

public class RtTransaction {

    /**
     * Returns the transaction id.
     *
     * @return the transaction id
     */
    public UncheckedScalar<String> transactionId() {
        return new UncheckedScalar<>(new IoCheckedScalar<>(this::transactionIdInternal));
    }

    private String transactionIdInternal() throws IOException {
        return "transactionId";
    }
}
```