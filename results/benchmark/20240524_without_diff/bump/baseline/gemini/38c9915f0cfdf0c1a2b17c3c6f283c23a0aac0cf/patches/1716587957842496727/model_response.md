```java
import org.cactoos.scalar.UncheckedScalar;

public class RtTransaction {
    public UncheckedScalar<String> id() {
        return new UncheckedScalar<>(() -> "transactionId");
    }
}
```