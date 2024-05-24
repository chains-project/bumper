Here's the proposed patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoCheckedBytes;
import org.cactoos.text.TextOfScalar;

// ...

public class RtNetwork {
    // ...

    @Override
    protected Scalar<byte[]> body() throws IOException {
        return new IoCheckedBytes(new TextOfScalar(super.body()));
    }
}
```

This patch replaces the usage of `IoCheckedScalar` with `IoCheckedBytes` and `TextOfScalar` from the new library version. It also introduces a new variable `TextOfScalar` to wrap the result of the `super.body()` call. The `IoCheckedBytes` constructor then takes this `TextOfScalar` and converts it to a `Scalar<byte[]>` as required by the method signature.