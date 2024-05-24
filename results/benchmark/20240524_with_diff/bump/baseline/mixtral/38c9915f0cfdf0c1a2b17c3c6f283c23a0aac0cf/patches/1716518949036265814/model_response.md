Here's a possible patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.IoChecked;
import org.cactoos.scalar.UncheckedScalar;

// ...

Scalar<InputStream> inputStreamScalar = // your scalar here
IoChecked<InputStream> ioCheckedInputStream = new IoChecked<>(inputStreamScalar, UncheckedScalar::new);
InputStream inputStream = ioCheckedInputStream.value();
// use inputStream here
```

The `IoCheckedScalar` class has been removed in the new library version. Instead, you can use the `IoChecked` class, which takes a `Scalar` and a `Func` as arguments. In this case, we use `UncheckedScalar::new` as the `Func` to convert the `Scalar` to an `UncheckedScalar`, which is then used to get the `InputStream`.