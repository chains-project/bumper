Here's the proposed patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarOf;

// ...

Scalar<Double> balance = new ScalarOf<>(() -> 100.0);

// Use ScalarOf instead of SolidScalar
Solid<Double> solidBalance = new Solid<>(balance);
```

In this patch, we replace the usage of `SolidScalar` with `ScalarOf` to create a `Solid` object. This should resolve the "cannot find symbol" error for `SolidScalar`.