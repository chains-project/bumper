```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TIOStreamTransport(null, os);
    ++framedTransport = new org.apache.thrift.transport.TFastFramedTransport(framedTransport, bufferCapacity);++
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```