```java
import org.cactoos.scalar.StickyScalar;

public class RtTransaction {

    private final StickyScalar<String> stickyScalar;

    public RtTransaction(StickyScalar<String> stickyScalar) {
        this.stickyScalar = stickyScalar;
    }

    public String getTransactionId() {
        return stickyScalar.value();
    }
}
```