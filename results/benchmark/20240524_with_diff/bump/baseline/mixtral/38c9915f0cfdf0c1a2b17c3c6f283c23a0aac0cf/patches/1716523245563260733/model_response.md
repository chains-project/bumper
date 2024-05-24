Here's a possible patch for the client code:

```java
import org.cactoos.bytes.CheckedBytes;
import java.util.function.Function;

// ...

CheckedScalar<Double> balance = new CheckedScalar<>(
  () -> new CheckedBytes(
    () -> new IoCheckedBytes(
      () -> new IoCheckedText(wallet.balance())
    ),
    s -> s.getBytes()
  ).asBytes(),
  Function.identity()
).value();
```

This patch uses the new `CheckedBytes` class introduced in the updated library version to read the balance of the `wallet` object as bytes, and then converts it to a `Double` value using the `Function.identity()` method. The `CheckedScalar` class is used to handle any exceptions that might occur during the conversion process.