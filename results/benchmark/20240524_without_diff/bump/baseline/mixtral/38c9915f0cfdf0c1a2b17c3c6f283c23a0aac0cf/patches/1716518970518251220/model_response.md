Here's the fixed version of the code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.IoChecked;

import java.io.IOException;

public class RtTransaction {
    // ...
    private Scalar<Bytes> bytes() throws IOException {
        return new IoChecked<>(
            () -> new ByteArrayResource(this.repository.load(this.id))
        );
    }
    // ...
}
```

In this patch, I replaced the usage of `IoCheckedScalar` with `IoChecked`, which is the new equivalent in the updated library version. The `IoChecked` class takes a `Callable` as a constructor argument, so I wrapped the `ByteArrayResource` creation in a lambda function to conform to the `Callable` interface.