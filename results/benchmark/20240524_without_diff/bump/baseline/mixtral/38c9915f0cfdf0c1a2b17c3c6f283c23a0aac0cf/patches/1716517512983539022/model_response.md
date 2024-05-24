Here's the patched version of the client code that fixes the error:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoChecked;
import org.cactoos.io.IoCheckedBytes;
import org.cactoos.io.InputOf;
import org.cactoos.text.IoCheckedText;
import org.cactoos.text.TextOf;
import org.cactoos.text.TextOfScalar;

// ...

public class WalletsIn {
    // ...

    @Override
    protected Scalar<InputStream> inputOf(final String address) {
        return new IoChecked<>(
            new InputOf(
                new IoCheckedText(
                    new TextOfScalar(
                        new UrlScalar(address)
                    )
                )
            )
        );
    }

    // ...
}
```

The changes made are:

1. Imported the necessary classes from the updated library version.
2. Replaced the usage of `IoCheckedScalar` with `IoChecked`.
3. Wrapped the `UrlScalar` inside a `TextOfScalar` to convert it to a `Text`.
4. Wrapped the `Text` inside an `IoCheckedText` to convert it to an `InputStream`.

This should resolve the "cannot find symbol" error caused by the removed `IoCheckedScalar` class.