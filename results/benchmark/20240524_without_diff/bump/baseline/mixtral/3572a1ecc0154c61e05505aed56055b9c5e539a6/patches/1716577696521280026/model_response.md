Here's the proposed patch for the failing method in `AppenderUtils.java`:

```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

import java.io.IOException;
import java.util.Properties;

public static TTransport createFastFramedTransport(Properties props) {
    String host = props.getProperty("thrift.transport.host");
    int port = Integer.parseInt(props.getProperty("thrift.transport.port"));

    TTransport transport = new TFastFramedTransport(host, port);

    try {
        transport.open();
    } catch (TTransportException e) {
        throw new IOException("Failed to open thrift transport", e);
    }

    return transport;
}
```

This patch replaces the usage of `TFastFramedTransport` with `TFastFramedTransport` from the `org.apache.thrift.transport` package, which is still available in the external dependency. The method signature remains unchanged.