```java
import org.cactoos.scalar.UncheckedScalar;
import org.cactoos.scalar.Unchecked;

public class RtTransaction {

    private final UncheckedScalar<String> rtTransactionId;

    public RtTransaction(String rtTransactionId) {
        this.rtTransactionId = new UncheckedScalar<>(rtTransactionId);
    }

    public String getRtTransactionId() {
        return rtTransactionId.value();
    }
}
```