```java
import org.cactoos.scalar.UncheckedScalar;

public class RtTransaction {

    public UncheckedScalar<String> rtTransaction(String txHash) {
        return () -> {
            throw new RuntimeException("Not implemented");
        };
    }
}
```