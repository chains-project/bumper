Here's a possible patch for the failing client code:
```java
import org.cactoos.Scalar;
import org.cactoos.scalar.IoChecked;
import org.cactoos.scalar.UncheckedScalar;

...

Scalar<Bytes> bytes = ... ; // your original bytes scalar

// Instead of using IoCheckedScalar, use IoChecked with an UncheckedScalar
IoChecked<Bytes> ioCheckedBytes = new IoChecked<>(new UncheckedScalar<>(bytes), IoChecked.None);
```
This code creates a new `IoChecked` instance using the `UncheckedScalar` wrapper for your original `bytes` scalar, and the `IoChecked.None` fallback. This should allow you to avoid using the removed `IoCheckedScalar` class and use the new `IoChecked` class instead.