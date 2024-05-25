Here is the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.io.InputOf;
import org.cactoos.scalar.UncheckedScalar;

Scalar<String> checkedIo(Scalar<InputOf> scalar) {
    return new UncheckedScalar<>(() -> scalar.value().asString());
}

@Override
public void load(String name) throws IOException {
    IoCheckedScalar<String> scalar = checkedIo(() -> new InputOf(
        new WalletFile(name)
    ));
    // use 'scalar' instead of 'new IoCheckedScalar<>(new InputOf(new WalletFile(name)))'
    // ...
}
```

This patch replaces the usage of the `IoCheckedScalar` class with a custom method `checkedIo` that creates an `UncheckedScalar` from a given `Scalar<InputOf>`. This allows us to avoid using the `IoCheckedScalar` class directly. The `checkedIo` method takes a `Scalar<InputOf>` as an argument, which is then used to create an `InputOf` instance for the `WalletFile` class. The resulting `InputOf` instance is then used to create an `UncheckedScalar` instance. This approach allows us to avoid using the `IoCheckedScalar` class directly, and instead use the `UncheckedScalar` class, which should be available in the new version of the library.