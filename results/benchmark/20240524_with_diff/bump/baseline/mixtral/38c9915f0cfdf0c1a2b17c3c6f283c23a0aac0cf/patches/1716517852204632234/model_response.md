Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Bytes> bytes = ...; // your original logic here

// Replace this line:
// UncheckedScalar<Bytes> usc = new UncheckedScalar<>(bytes);

// With these lines:
Scalar<Bytes> sc = new ScalarEnvelope<>(bytes);
UncheckedScalar<Bytes> usc = new UncheckedScalar<>(sc);
```

The patch creates a new `ScalarEnvelope` to wrap the original `bytes` scalar, and then wraps it again with `UncheckedScalar`. This way, you can keep the same method signature and avoid using the removed `UncheckedScalar` constructor directly.