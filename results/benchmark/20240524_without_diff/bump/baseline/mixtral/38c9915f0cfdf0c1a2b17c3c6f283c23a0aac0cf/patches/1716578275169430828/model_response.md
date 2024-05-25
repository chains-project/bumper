Here's a patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.UncheckedScalar;

Scalar<String> scalar = () -> "some value";
SolidScalar<String> solidScalar = new UncheckedScalar<>(scalar);
```

This patch replaces the failing import statement with the correct one and creates a new `SolidScalar` instance using the `UncheckedScalar` class. The `UncheckedScalar` class is a new addition in the library that can be used to wrap a `Scalar` instance, which is a part of the Cactoos library and a super-interface for `SolidScalar`.