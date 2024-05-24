Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Unchecked;

// ...

private Scalar<Transaction> unchecked(Transaction transaction) {
  return new Unchecked<>(transaction);
}
```

This patch replaces the usage of `UncheckedScalar` with `Unchecked`, which is a new class added in the updated library version. The `Unchecked` class can be used to wrap a scalar value, similar to how `UncheckedScalar` was used before. The `unchecked` method is updated to use `Unchecked` instead of `UncheckedScalar`.