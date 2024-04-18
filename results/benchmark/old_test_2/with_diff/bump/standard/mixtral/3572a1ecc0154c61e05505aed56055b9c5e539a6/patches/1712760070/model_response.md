Here's the proposed patch:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift log.
    final int bufferCapacity = 10;
    TConfiguration tConfig = new TConfiguration();
    TIOStreamTransport transport = new TIOStreamTransport(tConfig, os);
    framedTransport = new TFastFramedTransport(transport, bufferCapacity);
    protocol = new TBinaryProtocol(framedTransport);
}
```

This patch creates a `TConfiguration` object for the `TIOStreamTransport` constructor that takes a `TConfiguration` and an `OutputStream`. This constructor was added in the new library version. Then, it creates a `TFastFramedTransport` object using the new `TIOStreamTransport` object and the specified buffer capacity.