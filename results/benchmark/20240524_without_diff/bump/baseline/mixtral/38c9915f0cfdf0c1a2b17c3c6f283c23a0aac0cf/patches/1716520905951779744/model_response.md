Here's a proposed patch for the failing code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.UncheckedScalar;

// ...

Scalar<Double> amount = new UncheckedScalar<>(() -> 5.0);
Solid<Double> solidAmount = new ScalarOf<>(() -> amount.value());
```

In the new version of the library, the `SolidScalar` class has been removed and replaced with the `ScalarOf` class, which takes a `java.util.concurrent.Callable` or a `org.cactoos.Func` as an argument. To create a `Solid` scalar, you can use the `ScalarOf` class with a `Func` that returns the value of the scalar.

In this example, I've created a `Scalar` with a value of 5.0, then used the `ScalarOf` class to create a `Solid` scalar from the `Scalar`. The `ScalarOf` class takes a `Callable` as an argument, which returns the value of the scalar. In this case, I've used a lambda expression that calls the `value()` method of the `Scalar` to get its value.

Note that the `UncheckedScalar` class is used to wrap the `Scalar` to ensure that any exceptions thrown by the `Scalar` are propagated properly.

You can replace the original line `SolidScalar<Double> solidAmount = new SolidScalar<>(amount);` with the new code to fix the error.