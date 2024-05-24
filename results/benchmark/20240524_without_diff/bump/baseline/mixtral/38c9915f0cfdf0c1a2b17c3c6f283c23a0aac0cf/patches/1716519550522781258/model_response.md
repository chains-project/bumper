Here's the fixed version of the code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.UncheckedScalar;

// ...

Scalar<Double> amount = new UncheckedScalar<>(() -> {
    // implementation of the scalar
});

// use amount instead of SolidScalar
```

In this fixed version, I've replaced the usage of `SolidScalar` with `Scalar` and used `UncheckedScalar` to implement the scalar. This should resolve the "cannot find symbol" error as `Scalar` is still present in the new library version.