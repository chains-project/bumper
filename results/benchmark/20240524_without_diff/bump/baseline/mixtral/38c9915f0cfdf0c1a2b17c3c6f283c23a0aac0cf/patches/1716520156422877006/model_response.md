Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Bytes> bytes = ...; // your original code that returns a Scalar<Bytes>

Scalar<Bytes> uncheckedBytes = new ScalarEnvelope<>(bytes) {
  @Override
  protected Bytes value() throws Exception {
    return super.value();
  }
};
```

This patch wraps the original `Scalar<Bytes>` in a `ScalarEnvelope` to convert it to an `UncheckedScalar`. The `ScalarEnvelope` class was added in the new library version, and it can be used to convert a checked scalar to an unchecked one. The `value()` method is overridden to simply return the value of the original scalar.