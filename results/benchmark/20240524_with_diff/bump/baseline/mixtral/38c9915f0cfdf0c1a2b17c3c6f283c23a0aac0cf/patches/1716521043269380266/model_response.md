Here's the fixed version of the code:

```java
import org.cactoos.Scalar;
import org.cactoos.IoCheckedBytes;
import org.cactoos.input.InputOf;

...

public class WalletsIn extends ScalarEnvelope {
...
    @Override
    protected Scalar<byte[]> value() throws IOException {
        final IoCheckedBytes input = IoCheckedBytes. swallow(
            new InputOf(new File(path))
        );
        return new ScalarOf<byte[]>() {
            @Override
            public byte[] value() throws IOException {
                return input.asBytes();
            }
        };
    }
...
}
```

In this patch, I replaced the `IoCheckedScalar` import with `IoCheckedBytes` and updated the code accordingly. The `IoCheckedScalar` class has been removed in the new library version, but `IoCheckedBytes` provides similar functionality. The `IoCheckedBytes.swallow()` method is used to convert a `CheckedBytes` to a `Scalar<byte[]>`. The `InputOf` class is used to convert a `File` to an `InputStream`. The `ScalarOf` class is used to convert the `InputStream` to a `Scalar<byte[]>`. The `asBytes()` method of `IoCheckedBytes` is used to get the byte array from the `CheckedBytes`.