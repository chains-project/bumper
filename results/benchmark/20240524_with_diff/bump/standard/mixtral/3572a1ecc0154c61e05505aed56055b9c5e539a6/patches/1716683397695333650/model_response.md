Here's the fixed `init` method:
```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFastFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os));
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
    framedTransport.setFramedTransportBufferSize(bufferCapacity);
}
```
The `TFastFramedTransport` constructor no longer accepts buffer size arguments, so we set the buffer size using the `setFramedTransportBufferSize` method after creating the transport.