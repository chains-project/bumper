```java
import org.cactoos.scalar.UncheckedScalar;
import org.cactoos.scalar.Unchecked;

import java.util.function.Function;

public class RtTransaction {

    // ... other methods ...

    /**
     * Creates a new transaction.
     *
     * @param function the function to execute in the transaction
     * @param <T>      the type of the result
     * @return the result of the function
     */
    public <T> T transaction(Function<UncheckedScalar<T>, T> function) {
        return function.apply(new UncheckedScalar<>(() -> {
            // ... transaction logic ...
        }));
    }

    // ... other methods ...

}
```