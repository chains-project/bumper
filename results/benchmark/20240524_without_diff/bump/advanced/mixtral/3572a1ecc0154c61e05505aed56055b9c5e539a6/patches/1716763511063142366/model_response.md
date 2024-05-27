Here's the proposed patch:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os));
    framedTransport.setFramedTransportBufferSize(bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```

This patch replaces the usage of `com.pinterest.singer.client.logback.TFastFramedTransport` with `org.apache.thrift.transport.TFramedTransport`, which is part of the Apache Thrift library. The buffer size is now set using the `setFramedTransportBufferSize` method.