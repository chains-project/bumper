```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    TIOStreamTransport streamTransport = new TIOStreamTransport(new org.apache.thrift.TConfiguration(), os);
    framedTransport = new com.pinterest.singer.client.logback.TFastFramedTransport(streamTransport, bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```