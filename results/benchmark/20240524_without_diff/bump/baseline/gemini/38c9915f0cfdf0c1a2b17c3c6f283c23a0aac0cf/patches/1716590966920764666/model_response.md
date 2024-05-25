```java
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Objects;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

public class RtTransaction {

    private final InputStream in;
    private final OutputStream out;

    public RtTransaction(InputStream in, OutputStream out) {
        this.in = in;
        this.out = out;
    }

    public void execute() throws IOException {
        try (GZIPInputStream gzipIn = new GZIPInputStream(in);
             GZIPOutputStream gzipOut = new GZIPOutputStream(out)) {
            gzipOut.write(gzipIn.readAllBytes());
        }
    }

    public static RtTransaction of(InputStream in, OutputStream out) {
        return new RtTransaction(Objects.requireNonNull(in), Objects.requireNonNull(out));
    }
}
```