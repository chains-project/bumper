Here's a possible patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.UncheckedScalar;

// ...

Scalar<Double> scalar = new UncheckedScalar<>(() -> 42.0);
double value = scalar.value();
```

In this patch, we're using the `UncheckedScalar` class to create a scalar that returns a `double` value. We then call the `value()` method to get the actual value. This should fix the "cannot find symbol" error you were seeing before.