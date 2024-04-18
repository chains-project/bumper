Here's the proposed patch:

```java
import org.apache.thrift.transport.TIOStreamTransport;

// ...

public static TFramedTransport newFastFramedTransport(TTransport transport) {
    return new TFastFramedTransport(transport);
}

// Usage example:
TIOStreamTransport ioStreamTransport = new TIOStreamTransport(new TConfiguration(), new ByteArrayInputStream(new byte[1024]));
TFramedTransport framedTransport = newFastFramedTransport(ioStreamTransport);
```

The `newFastFramedTransport` method creates a new `TFastFramedTransport` instance using the `TIOStreamTransport` constructor introduced in the new library version. This way, the code doesn't rely on the removed constructors.

Replace the usage of the removed constructors with the new method to fix the issue.