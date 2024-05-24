Here's the proposed patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.io.InputOf;

import java.io.IOException;

public class WalletsIn {
    ...
    private Scalar<Iterable<String>> wallets() throws IOException {
        return new IoCheckedBytes(
            new InputOf("..."),
            bytes -> new String(bytes, "UTF-8").lines()
        );
    }
    ...
}
```

Here, I replaced `IoCheckedScalar` with `IoCheckedBytes` and used its `asBytes()` method to get the bytes and convert them to a string.

Additionally, you need to include the new dependency version in your project configuration.