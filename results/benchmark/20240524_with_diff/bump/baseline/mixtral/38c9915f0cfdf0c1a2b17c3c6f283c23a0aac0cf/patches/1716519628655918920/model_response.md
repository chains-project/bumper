Here's the fixed version of the code:

```java
import org.cactoos.Scalar;
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.io.InputOf;
import org.cactoos.io.ResourceOf;
import org.cactoos.text.TextOf;
import org.cactoos.text.TextOfScalar;
import java.io.IOException;

public class WalletsIn {
    ...

    private Scalar<String> content(final String path) throws IOException {
        return new ScalarOf<String>(
            () -> new TextOfScalar(
                new IoCheckedBytes(
                    new ResourceOf(path),
                    InputOf::new
                )
            ).asString()
        );
    }

    ...
}
```

The changes made are:

1. Replace `import org.cactoos.scalar.IoCheckedScalar;` with `import org.cactoos.bytes.IoCheckedBytes;` and `import org.cactoos.io.InputOf;` for using the `IoCheckedBytes` class to read files.
2. Replace `org.cactoos.scalar.IoCheckedScalar` with `org.cactoos.bytes.IoCheckedBytes` in the `content` method.
3. Replace `org.cactoos.text.TextOf` with `org.cactoos.text.TextOfScalar` in the `content` method.
4. Add `import org.cactoos.text.TextOfScalar;` for using `TextOfScalar` class.
5. Remove the unused `import org.cactoos.Scalar$NoNulls;` import statement.

These changes should resolve the "cannot find symbol" error related to `IoCheckedScalar`.