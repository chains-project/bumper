Here's a possible patch for the failing code:
```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Double> balance = new ScalarEnvelope<>(() -> {
    // Calculate the balance here
});
UncheckedScalar<Double> uncheckedBalance = new Unchecked<>(balance);
```
In this patch, we're using the new `ScalarEnvelope` class to create a scalar that wraps a function that calculates the balance. We then pass this scalar to the `Unchecked` constructor to create an `UncheckedScalar` that can be used in the same way as before.

Note that we're using the `Scalar` interface instead of the concrete `UncheckedScalar` class, since the latter has been removed in the new library version. We're also using a lambda expression to define the function that calculates the balance. You'll need to replace the lambda expression with your own code to calculate the balance.

Additionally, note that we're importing the `org.cactoos.scalar.ScalarEnvelope` class and the `org.cactoos.scalar.Unchecked` class. These are new classes that have been added in the new library version. We're using `ScalarEnvelope` to create a scalar that wraps a function that calculates the balance, and we're using `Unchecked` to create an `UncheckedScalar` that can be used in the same way as before.

Finally, note that we're using the `UncheckedScalar` class instead of the `UncheckedScalar` interface. This is because the `UncheckedScalar` interface has been removed in the new library version, and the `UncheckedScalar` class has been added instead. We're using the `UncheckedScalar` class to create an object that can be used in the same way as the old `UncheckedScalar` interface.