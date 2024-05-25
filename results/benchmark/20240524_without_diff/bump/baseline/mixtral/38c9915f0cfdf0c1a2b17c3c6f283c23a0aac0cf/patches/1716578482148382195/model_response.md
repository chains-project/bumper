Here's a patch that you can apply to the code in order to fix the error:

```java
import org.cactoos.Scalar;
import org.cactoos.io.InputOf;
import org.cactoos.scalar.UncheckedScalar;

@Override
public Double balance(String address) throws IOException {
    Scalar<Input> scalar = () -> new InputOf(
        new URL(String.format(
            "http://localhost:8080/api/wallets/%s/balance",
            address
        )).openStream()
    );
    return new UncheckedScalar<>(scalar).value();
}
```

In this patch, I replaced the `IoCheckedScalar` class with a combination of `Scalar`, `UncheckedScalar`, and a lambda function that creates an `Input` object from a URL. This should resolve the "cannot find symbol" error that you encountered.