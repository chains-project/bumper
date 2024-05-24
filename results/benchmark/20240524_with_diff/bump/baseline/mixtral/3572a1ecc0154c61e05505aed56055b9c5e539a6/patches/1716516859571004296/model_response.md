Here's the proposed patch:

```java
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.InputStream;
import java.io.OutputStream;

public class AppenderUtils {
    // ...

    @Override
    protected TTransport createTransport(InputStream inputStream, OutputStream outputStream) {
        return new TIOStreamTransport(new TConfiguration(), inputStream, outputStream);
    }

    // ...
}
```

This patch replaces the usage of `TFramedTransport` with `TIOStreamTransport`, which is a new addition in the updated library version. The `TIOStreamTransport` constructor with `TConfiguration`, `InputStream`, and `OutputStream` parameters is used to ensure compatibility with the existing method signature.