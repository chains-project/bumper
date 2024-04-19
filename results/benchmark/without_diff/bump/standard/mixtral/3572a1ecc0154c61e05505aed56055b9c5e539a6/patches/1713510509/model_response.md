Here's a fixed version of the `init` method that uses the added `TFramedTransport` class instead of `TFastFramedTransport`:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new com.pinterest.singer.client.logback.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os), bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```

Note that I replaced `TFastFramedTransport` with `TFramedTransport`, which is an added library method. This should fix the error you're seeing.