Here's a fixed version of the failing method using the new TFramedTransport constructor:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    TTransport transport = new org.apache.thrift.transport.TIOStreamTransport(os);
    framedTransport = new org.apache.thrift.transport.TFramedTransport(transport, bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```

The TFastFramedTransport class has been removed in the new library version. I replaced it with the TFramedTransport constructor, which takes a TTransport and an integer parameter.