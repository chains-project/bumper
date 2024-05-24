Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Bytes> bytes = ...; // your original bytes scalar
Scalar<Bytes> uncheckedBytes = new ScalarEnvelope<>(bytes);
```

In this patch, I replaced the usage of `UncheckedScalar` with `ScalarEnvelope`, which is an added class in the new library version. This will allow you to wrap your original `Scalar<Bytes>` object and use it in the same way as before.