Here's the proposed patch for the failing client code:

```java
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.InputStream;
import java.io.OutputStream;

public class AppenderUtils {
    // ...

    private static TTransport createTransport(TConfiguration conf, InputStream in, OutputStream out) {
        return new TIOStreamTransport(conf, in, out);
    }

    private static TTransport createTransport(TConfiguration conf, OutputStream out) {
        return new TIOStreamTransport(conf, out);
    }

    // ...
}
```

This patch replaces the usage of `TFramedTransport` with `TIOStreamTransport` since the framed transport has been removed in the new library version. Also, two methods are added to create `TIOStreamTransport` instances based on the provided `TConfiguration`, `InputStream`, and `OutputStream`.