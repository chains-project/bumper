Here's the proposed patch for the failing method in `AppenderUtils.java`:

```java
import org.apache. thrift.transport.TTransport;
import org.apache. thrift.transport.TTransportException;

private static TTransport createFastFramedTransport(InputStream input) {
    TTransport transport = new TFramedTransport(new TTransport(input));
    try {
        transport.open();
    } catch (TTransportException e) {
        throw new RuntimeException("Failed to open transport", e);
    }
    return transport;
}
```

In this patch, I've replaced the import statement with a more generic one for `TTransport` and replaced the specific `TFastFramedTransport` import with it. I've also updated the method's implementation to create a `TFramedTransport` using the more generic `TTransport` constructor.

Note: This patch assumes that the input parameter `input` is an instance of `InputStream`.