Here's the patched version of the client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.IoChecked;
import org.cactoos.scalar.UncheckedScalar;

// ...

public IoChecked<InputStream> input(String id) throws IOException {
  Scalar<InputStream> scalar = () -> inputOf(id);
  return new IoChecked<>(new UncheckedScalar<>(scalar), this::closeQuietly);
}
```

The changes made are as follows:

1. Imported the `IoChecked` class from `org.cactoos.scalar` package.
2. Imported the `UncheckedScalar` class from `org.cactoos.scalar` package.
3. Replaced the usage of `IoCheckedScalar` with `IoChecked` and `UncheckedScalar`.

This patch ensures that the client code continues to work correctly with the new library version.