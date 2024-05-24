Here's the patched code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Sticky;

import static java.util.Collections.singletonList;

public class RtTransaction {
    ...
    private Sticky<Double> amount() {
        return new Sticky<>(
            () -> new NumberOfScalars(
                new ScalarOfSupplier(() -> fee()),
                new ScalarOfSupplier(() -> value())
            ).doubleValue()
        );
    }
    ...
}
```

Changes made:

- Imported `org.cactoos.Scalar` and `org.cactoos.scalar.Sticky`.
- Replaced the usage of `StickyScalar` with `Sticky`.
- Wrapped the `fee()` and `value()` calls inside a `ScalarOfSupplier` to convert them into `Scalar` instances.
- Wrapped the resulting `Scalar` instances inside a `NumberOfScalars` to calculate the sum.
- Wrapped the `NumberOfScalars` inside a `Sticky` to make it sticky.

Note: I assumed that `fee()` and `value()` methods return `Scalar` instances. If they don't, you might need to adjust the code accordingly.