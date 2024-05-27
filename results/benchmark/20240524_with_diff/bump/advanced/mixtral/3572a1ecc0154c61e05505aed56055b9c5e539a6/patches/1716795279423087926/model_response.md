Here's a patch that you can apply to the failing client code:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os), bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```

In this patch, I replaced the `TFastFramedTransport` class with `TFramedTransport`, which is the recommended class for framed transport in Apache Thrift. This should fix the "cannot find symbol" error that you encountered.