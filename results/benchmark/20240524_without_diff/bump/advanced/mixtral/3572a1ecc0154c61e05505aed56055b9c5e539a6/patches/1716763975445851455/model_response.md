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

In this patch, I replaced the `TFastFramedTransport` with `TFramedTransport` from the `org.apache.thrift.transport` package. The `bufferCapacity` is removed since `TFramedTransport` does not require it as a constructor argument. The `TIOStreamTransport` is still used as the input/output stream transport. The `TBinaryProtocol` is kept unchanged.