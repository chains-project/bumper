Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Double> balance = new ScalarEnvelope<>(() -> {
    // balance calculation here
});
```

This patch replaces the usage of `UncheckedScalar` with `ScalarEnvelope`, which is a new class introduced in the updated library version. The `ScalarEnvelope` class can be used to wrap a supplier function that computes the scalar value, similar to how `UncheckedScalar` was used.