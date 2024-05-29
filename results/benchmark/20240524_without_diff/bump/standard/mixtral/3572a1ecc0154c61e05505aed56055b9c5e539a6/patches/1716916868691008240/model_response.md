Here's the proposed patch:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os));
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```

In this patch, I replaced the `TFastFramedTransport` with `TFramedTransport` from the `org.apache.thrift.transport` package. This should resolve the error message about the `TFastFramedTransport` symbol not being found. I also removed the `bufferCapacity` argument since it is not used by `TFramedTransport`.