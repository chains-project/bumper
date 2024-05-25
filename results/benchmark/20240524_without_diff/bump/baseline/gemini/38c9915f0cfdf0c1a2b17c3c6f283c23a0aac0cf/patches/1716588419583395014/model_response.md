```java
  import org.cactoos.scalar.UncheckedScalar;
import org.cactoos.scalar.Unchecked;
import org.jetbrains.annotations.NotNull;

import java.util.concurrent.CompletableFuture;

public class RtTransaction {
    public CompletableFuture<String> getRtTransaction(@NotNull String id) {
        return new UncheckedScalar<CompletableFuture<String>>(
                () -> RtTransaction.super.getRtTransaction(id)
        ).value();
    }
}
```