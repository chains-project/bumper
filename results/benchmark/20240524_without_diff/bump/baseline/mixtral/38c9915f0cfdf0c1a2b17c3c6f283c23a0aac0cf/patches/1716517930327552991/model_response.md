Here's the patch to fix the error:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Unchecked;

// ...

Scalar<Bytes> bytes = ...; // your original logic here

// Replace the following line:
// Bytes data = new UncheckedScalar<>(bytes).value();

Bytes data = new Unchecked<>(bytes).value();
```

The change here is to replace the `UncheckedScalar` import with `Unchecked` import and update the instantiation accordingly.