Here's a fixed version of the code that replaces the deprecated `TFramedTransport` with the recommended `TFramedTransport` from the `netty` package. Note that you'll need to include the Netty dependencies in your project for this to work.

```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.transport.TTransport transport = null;
    try {
        transport = new org.apache.thrift.transport.netty.TFramedTransport(new org.apache.thrift.transport.TSocket("localhost", 9090));
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TCompactProtocol.Factory(), transport);
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```

This code uses `org.apache.thrift.transport.netty.TFramedTransport` instead of `org.apache.thrift.transport.TFramedTransport`. The `netty` package is recommended for new projects, as it provides better performance and scalability.