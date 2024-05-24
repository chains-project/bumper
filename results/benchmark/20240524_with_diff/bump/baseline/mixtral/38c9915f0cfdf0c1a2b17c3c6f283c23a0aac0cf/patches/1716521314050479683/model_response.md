Here's a patch that you can apply to fix the error:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Unchecked;

// ...

Scalar<Bytes> bytes = new Unchecked<>(() -> ...);
```

In this patch, we replace the usage of `UncheckedScalar` with `Unchecked`, which is a new class added in the updated library version. We then use the `Unchecked` class to create a `Scalar` of `Bytes`, which can be used in place of the original `UncheckedScalar`.