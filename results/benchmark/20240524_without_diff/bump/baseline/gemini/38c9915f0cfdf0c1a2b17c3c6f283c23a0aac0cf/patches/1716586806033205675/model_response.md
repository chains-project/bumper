```java
import org.cactoos.scalar.UncheckedScalar;

import java.util.concurrent.CompletableFuture;

public class RtTransaction {

    private final CompletableFuture<UncheckedScalar<String>> txId;

    public RtTransaction(CompletableFuture<UncheckedScalar<String>> txId) {
        this.txId = txId;
    }

    public CompletableFuture<UncheckedScalar<String>> getTxId() {
        return txId;
    }

}
```