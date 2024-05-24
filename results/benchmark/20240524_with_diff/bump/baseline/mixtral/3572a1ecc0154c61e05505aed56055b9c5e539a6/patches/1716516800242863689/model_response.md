Here's the proposed patch:

```java
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.InputStream;
import java.io.OutputStream;

public class AppenderUtils {
    // ...

    @Override
    protected TTransport createTransport(TConfiguration conf, InputStream in, OutputStream out) {
        return new TIOStreamTransport(conf, in, out);
    }

    // ...
}
```

This patch replaces the usage of `TFramedTransport` with `TIOStreamTransport`, which is a new addition in the updated library version. The `createTransport` method is updated to accept the required parameters for creating a `TIOStreamTransport` instance. Note that the `TIOStreamTransport` constructor with `TConfiguration` as a parameter is protected, so we need to use the constructor with both `InputStream` and `OutputStream` to create an instance.