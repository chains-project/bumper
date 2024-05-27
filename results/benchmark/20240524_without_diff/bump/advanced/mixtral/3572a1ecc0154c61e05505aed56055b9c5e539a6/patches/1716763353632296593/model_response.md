Here's the patched method:
```java
@Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os), bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```
I replaced `com.pinterest.singer.client.logback.TFastFramedTransport` with `org.apache.thrift.transport.TFramedTransport`.
This is because `TFastFramedTransport` seems to be an internal class of the `singer` project, and it's not part of the public API.
Instead, the public API provides `TFramedTransport` which should be sufficient for framing thrift messages.