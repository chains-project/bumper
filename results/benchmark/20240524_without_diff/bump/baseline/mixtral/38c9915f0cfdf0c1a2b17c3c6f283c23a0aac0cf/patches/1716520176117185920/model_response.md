Here's a patch that you can apply to fix the error:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Integer> scalar = new ScalarEnvelope<Integer>(() -> 42);
```

This code creates a `Scalar` instance that always returns the value `42` when its `value()` method is called. The `ScalarEnvelope` class is used to create a new `Scalar` instance that wraps another `Scalar`. In this case, we're using a lambda expression to provide the implementation of the wrapped `Scalar`.

You can replace the usage of `UncheckedScalar` with `ScalarEnvelope` in your code. If you need to create a `Scalar` instance that may throw an exception, you can use `CheckedScalar` instead.

Note that the `UncheckedScalar` class has been removed in the new version of the library, so it can no longer be used. The `ScalarEnvelope` class provides similar functionality and should be used instead.