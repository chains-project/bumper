Here's the proposed patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.UncheckedScalar;

Scalar<Double> amount() {
    return new UncheckedScalar<>(new SolidScalar<>(100.0));
}
```

This patch replaces the import statement for `SolidScalar` with the more general `Scalar` interface from the same library. It then creates a new `UncheckedScalar` instance that wraps the `SolidScalar` instance. This allows the code to continue using the same functionality as before while avoiding the error caused by the external dependency update.