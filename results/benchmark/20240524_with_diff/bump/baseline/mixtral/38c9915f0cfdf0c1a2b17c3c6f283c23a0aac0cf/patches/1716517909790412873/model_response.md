Here's a possible patch for the failing code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.UncheckedScalar;

Scalar<String> scalar = () -> "some value";
UncheckedScalar<String> uncheckedScalar = new UncheckedScalar<>(scalar);
```

This code creates a `Scalar` instance using a lambda expression, and then wraps it in an `UncheckedScalar` instance. The `UncheckedScalar` class is still present in the new library version, so it can still be used.

Note that I had to make a few assumptions about the type of the scalar value, since it was not specified in the original code. You may need to adjust the type of the `Scalar` and `UncheckedScalar` instances to match your specific use case.