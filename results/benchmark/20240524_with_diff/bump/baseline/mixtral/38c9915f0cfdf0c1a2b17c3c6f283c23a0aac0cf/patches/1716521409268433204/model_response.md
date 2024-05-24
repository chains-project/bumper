Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Unchecked;

// ...

private Scalar<Transaction> unchecked(Transaction transaction) {
  return new Unchecked<>(transaction);
}
```

This patch replaces the usage of `UncheckedScalar` with `Unchecked`, which is a new class added in the updated library version. The `Unchecked` class serves a similar purpose as `UncheckedScalar`, but it is now used to wrap a `Scalar` instead of a raw object.