Here's a suggested patch for the client code:

```java
import org.cactoos.io.Joined;
import org.cactoos.text.TextOf;

...

public class WalletsIn extends Wallets {
    ...

    @Override
    protected Input stream(final WalletId id) throws IOException {
        return new Joined(
            Arrays.stream(
                new TextOf(id.value()),
                new TextOf(":"),
                super.stream(id)
            )
            .map(TextOf::new)
            .toArray(TextOf[]::new)
        );
    }
}
```

This patch replaces the usage of `JoinedText` with `Joined` from the `org.cactoos.io` package. The `Joined` class can take an iterable of `Input` objects, which are created from the `TextOf` objects. The resulting `Input` is then returned.

Note: This patch assumes that the `WalletId` class has a `value()` method that returns a `String` representation of the wallet ID.