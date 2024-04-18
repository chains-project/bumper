Here's the proposed patch for the failing method in `AppenderUtils.java`:

```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

public static TTransport createFastFramedTransport(InputStream input) throws TTransportException {
    return new TFastFramedTransport(input, 65536, 65536);
}
```

This patch replaces the usage of `TFastFramedTransport` with `TTransport`, which is the base interface for all Thrift transports. The `createFastFramedTransport` method is re-implemented to return a `TFastFramedTransport` instance, which should work with the new version of the external dependency.