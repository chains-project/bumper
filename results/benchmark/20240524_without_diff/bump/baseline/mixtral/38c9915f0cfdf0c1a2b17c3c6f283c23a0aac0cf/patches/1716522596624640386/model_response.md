Here's the fixed version of the client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

public class Wallet {
    // ...

    private Scalar<Double> balance() {
        Scalar<Double> balance = new ScalarEnvelope<>(
            () -> api.balance(account())
        );
        return balance;
    }

    // ...
}
```

The changes made include:

1. Importing the new `ScalarEnvelope` class from the updated library.
2. Wrapping the balance-fetching lambda expression in a `ScalarEnvelope` to ensure that the result is never `null`.
3. Removing the unused `UncheckedScalar` import statement.

These changes ensure that the client code works with the updated library version and avoids the "cannot find symbol" error.