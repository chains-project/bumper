Here's the proposed patch:

```java
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.InputStream;
import java.io.OutputStream;

public class AppenderUtils {
    // ...

    @Override
    protected TTransport createTransport(TConfiguration conf, String transportType) throws TTransportException {
        if (transportType.equalsIgnoreCase("framed")) {
            return new TFastFramedTransport(new TIOStreamTransport(conf, new ByteArrayInputStream(new byte[0]), new ByteArrayOutputStream()));
        }
        // ...
    }

    // ...
}
```

This patch replaces the usage of the removed `TFastFramedTransport$Factory` methods with the new `TIOStreamTransport` constructor. The `TIOStreamTransport` is used to create a `TFastFramedTransport`.