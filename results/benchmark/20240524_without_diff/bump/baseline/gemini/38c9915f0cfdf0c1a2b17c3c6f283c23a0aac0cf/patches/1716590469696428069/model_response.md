```java
import org.cactoos.scalar.StickyScalar;

public class RtTransaction {

    public RtTransaction(StickyScalar<String> transactionId) {
        this.transactionId = transactionId;
    }

    private final StickyScalar<String> transactionId;

    public String getTransactionId() {
        return transactionId.value();
    }
}
```