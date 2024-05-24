Here's the fixed version of the code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Double> balance = new ScalarEnvelope<>(() -> api.balance(walletId));
```

This code replaces the use of `UncheckedScalar` with a new class `ScalarEnvelope` that achieves the same goal. The class wraps a function that produces a value, and the value can be accessed using the `value()` method.

Note that the type of the `balance` variable has been changed from `UncheckedScalar<Double>` to `Scalar<Double>`. This is necessary because `UncheckedScalar` is no longer available in the updated library version. However, `Scalar` is a superclass of `UncheckedScalar`, so any code that uses `UncheckedScalar` can be easily modified to use `Scalar` instead.