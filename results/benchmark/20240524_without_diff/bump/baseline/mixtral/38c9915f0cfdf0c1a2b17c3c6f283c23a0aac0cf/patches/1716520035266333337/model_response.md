Here's the patched code that fixes the error:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.NoNulls;

// ...

private Scalar<Transaction> scalar(String hash) {
  return new NoNulls<>(() -> db().transaction(hash));
}
```

The patch replaces the usage of `UncheckedScalar` with `NoNulls`, which is a new class in the updated library version. The `NoNulls` class can be used to ensure that the result of the provided `Scalar` is not `null`.