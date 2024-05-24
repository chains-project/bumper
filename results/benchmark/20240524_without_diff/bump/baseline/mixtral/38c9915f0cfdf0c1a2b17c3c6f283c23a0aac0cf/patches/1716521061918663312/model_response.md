Here's the fixed version of the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoChecked;
import org.cactoos.io.IoCheckedBytes;
import org.cactoos.io.IoCheckedText;
import org.cactoos.text.TextOfScalar;

import java.io.IOException;

public final class WalletsIn {
    // ...

    private Scalar<String> loadWallets(final Scalar<String> content) throws IOException {
        return new IoChecked<>(
            new IoCheckedBytes(
                new IoCheckedText(
                    new TextOfScalar(content)
                ),
                IoCheckedText::asBytes
            ),
            IoCheckedBytes::value
        );
    }

    // ...
}
```

This version replaces the missing `IoCheckedScalar` with the new `IoChecked` and `IoCheckedBytes` classes, along with the new `TextOfScalar` and `IoCheckedText` classes. It also uses a `Scalar` instead of the removed `UncheckedScalar`. This should resolve the "cannot find symbol" error.