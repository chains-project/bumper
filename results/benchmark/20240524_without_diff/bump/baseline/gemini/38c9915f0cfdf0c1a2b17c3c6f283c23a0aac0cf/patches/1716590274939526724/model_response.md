```java
import org.cactoos.scalar.StickyScalar;

public class RtTransaction {

    public StickyScalar<String> getTransactionId() {
        return new StickyScalar<>(() -> {
            return String.valueOf(System.currentTimeMillis());
        });
    }
}
```