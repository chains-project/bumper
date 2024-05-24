Here's the patched version of the client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.NoNulls;

// ...

public RtTransaction(String id, Scalar<Transaction> tx) {
  this.id = id;
  this.tx = new NoNulls<>(tx); // use NoNulls instead of UncheckedScalar
}
```

In the new version of the library, `UncheckedScalar` has been removed and replaced with `NoNulls`. In this patch, we replace the usage of `UncheckedScalar` with `NoNulls`, ensuring the client code continues to function correctly.