Here's the proposed patch for the failing method in `AppenderUtils.java`:

```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

public static TTransport createFastFramedTransport(InputStream inputStream) throws TTransportException {
    TFastFramedTransport transport = new TFastFramedTransport(inputStream, 65536, 65536);
    transport.open();
    return transport;
}
```

This patch replaces the failing import statement and updates the `TFastFramedTransport` instantiation to use the new import. The method signature remains unchanged.