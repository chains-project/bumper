```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    TConfiguration conf = new TConfiguration();
    // Use the newly added constructor with TConfiguration for TIOStreamTransport
    TIOStreamTransport transport = new TIOStreamTransport(conf, os);
    framedTransport = new com.pinterest.singer.client.logback.TFlushingFastFramedTransport(transport, bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```