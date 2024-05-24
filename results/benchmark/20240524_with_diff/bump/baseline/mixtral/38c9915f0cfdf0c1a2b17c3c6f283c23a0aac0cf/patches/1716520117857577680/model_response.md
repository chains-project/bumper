Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

private Scalar<Transaction> unchecked(Transaction transaction) {
  return new ScalarEnvelope<>(transaction);
}
```

This patch wraps the `Transaction` object in a `ScalarEnvelope`, which implements the `Scalar` interface required by the method signature.