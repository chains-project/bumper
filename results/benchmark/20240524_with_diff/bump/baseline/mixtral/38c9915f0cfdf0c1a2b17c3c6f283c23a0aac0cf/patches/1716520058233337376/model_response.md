Here's the patched version of the client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.NoNulls;

// ...

Scalar<Bytes> bytes = ...;
NoNulls<Bytes> uncheckedBytes = new NoNulls<>(bytes);
Bytes value = uncheckedBytes.value();
```

This code replaces the usage of `UncheckedScalar` with `NoNulls`, which is a new class in the updated library version. The `NoNulls` class ensures that the provided `Scalar` never returns `null`. In this case, it's used to wrap a `Scalar<Bytes>` instance, and the `value()` method is called on the resulting object to get the actual value.