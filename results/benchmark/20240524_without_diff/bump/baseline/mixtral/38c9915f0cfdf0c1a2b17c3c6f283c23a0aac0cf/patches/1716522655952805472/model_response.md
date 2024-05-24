Here's a possible patch for the failing code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Double> balance = new ScalarEnvelope<>(() -> {
    // ...
});
```

This patch replaces the use of `UncheckedScalar` with `ScalarEnvelope`, which is a new class added in the updated library version. The `ScalarEnvelope` class provides a way to create a scalar that can throw exceptions, similar to `UncheckedScalar`. In this patch, I've assumed that the original `UncheckedScalar` was used to create a scalar that returns a `double` value, so I've used `ScalarEnvelope<Double>` to replace it. You can adjust the type argument of `ScalarEnvelope` based on the actual type of the value returned by the original `UncheckedScalar`.

Note that I've also changed the name of the variable from `uncheckedBalance` to `balance` to reflect the fact that the new variable is no longer an "unchecked" scalar. You can adjust the name of the variable to fit your naming conventions.