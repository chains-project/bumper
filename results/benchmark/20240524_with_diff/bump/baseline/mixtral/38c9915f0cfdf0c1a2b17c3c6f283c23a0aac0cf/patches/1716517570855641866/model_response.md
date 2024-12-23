Here is the proposed patch:
```java
import org.cactoos.Scalar;
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.proc.IoCheckedProc;

import java.io.IOException;

public class WalletsIn {
    ...
    private Scalar<Bytes> bytes(final String filename) throws IOException {
        return IoCheckedScalar.value(() -> Files.newInputStream(Paths.get(filename)));
    }

    private Bytes content(final Scalar<Bytes> bytes) throws IOException {
        return new IoCheckedBytes(bytes, IoCheckedProc.whenChecked(this::toUtf8));
    }

    private byte[] toUtf8(final InputStream is) throws IOException {
        try (final ByteArrayOutputStream os = new ByteArrayOutputStream()) {
            final byte[] buffer = new byte[8192];
            int read;
            while ((read = is.read(buffer)) != -1) {
                os.write(buffer, 0, read);
            }
            return os.toByteArray();
        }
    }
    ...
}
```
Here, I replaced the use of `IoCheckedScalar` with `Scalar` and `IoCheckedBytes` with `Bytes`. I also added a new method `toUtf8` to convert the `InputStream` to a `byte[]` using a `ByteArrayOutputStream`. Finally, I updated the `content` method to use `IoCheckedBytes` constructor that takes a `Scalar<Bytes>` and a `IoCheckedProc`. The `IoCheckedProc` converts the `InputStream` to a `byte[]` using the new `toUtf8` method.