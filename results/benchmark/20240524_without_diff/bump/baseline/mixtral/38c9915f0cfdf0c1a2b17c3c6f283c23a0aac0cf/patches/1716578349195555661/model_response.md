Here's the proposed patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.UncheckedScalar;

Scalar<Double> solidScalar(Double value) {
  return new UncheckedScalar<>(() -> value);
}
```

This patch replaces the usage of `SolidScalar` with `UncheckedScalar`, which is a part of the Cactoos library and has a similar functionality. The `solidScalar` method creates a scalar object that always returns the provided value. This should fix the "cannot find symbol" error.