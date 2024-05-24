Here's the proposed patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Integer> scalar = ...; // your original scalar value
ScalarEnvelope<Integer> scalarEnvelope = new ScalarEnvelope<>(scalar);
int value = scalarEnvelope.value();
```

In this patch, I replaced the usage of `UncheckedScalar` with `ScalarEnvelope`, which is an added class in the new library version. The `ScalarEnvelope` class ensures that the scalar value is not null, providing a safer alternative. The `value()` method is used to extract the scalar value.