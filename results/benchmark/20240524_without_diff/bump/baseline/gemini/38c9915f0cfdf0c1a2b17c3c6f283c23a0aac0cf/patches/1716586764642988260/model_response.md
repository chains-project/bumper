```java
import org.cactoos.scalar.UncheckedScalar;

import java.util.function.Function;

public class RtTransaction {

    public static <T> UncheckedScalar<T> of(Function<RtTransaction, T> func) {
        return new UncheckedScalar<>(func);
    }

}
```