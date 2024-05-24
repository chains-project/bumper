Here's a possible patch for the failing client code:

```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.input.InputOf;
import org.cactoos.text.TextOf;
import org.cactoos.Scalar;

public class RtTransaction {
    // ...
    private Scalar<String> loadTransaction(final String id) {
        return new IoCheckedScalar<>(
            new InputOf(
                new IoCheckedBytes(
                    new BytesOf(
                        new TextOfScalar(
                            loadTransaction0(id)
                        )
                    )
                )
            ),
            InputOf::asString
        );
    }
    // ...
}
```

This patch replaces the failing `IoCheckedScalar` import with the new `IoCheckedBytes` and `TextOfScalar` classes. It also wraps the `loadTransaction0` method call with a `TextOfScalar` to convert the result to a `Scalar<String>`. Finally, it wraps the `IoCheckedBytes` with an `InputOf` to convert it to an `Input<String>`, which can then be passed to the `IoCheckedScalar` constructor.