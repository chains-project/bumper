Here's the patched version of the client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Unchecked;

// ...

Scalar<Bytes> bytes = ...;
Bytes data = new Unchecked<>(bytes).value();
```

The `UncheckedScalar` class has been removed in the new library version, so I replaced it with the `Unchecked` class, which achieves the same goal. I also changed the type of the `bytes` variable from `UncheckedScalar<Bytes>` to `Scalar<Bytes>` and used the `value()` method of the `Unchecked` class to extract the bytes.