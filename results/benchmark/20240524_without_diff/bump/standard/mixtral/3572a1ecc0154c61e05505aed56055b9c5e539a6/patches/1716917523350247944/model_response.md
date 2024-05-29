Here's a fixed version of the method using `TNonblockingServerTransport` instead of the deprecated `TFramedTransport`. This should resolve the compilation error.

```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.transport.TTransport transport = null;
    try {
        transport = new org.apache.thrift.transport.TNonblockingServerTransport(new org.apache.thrift.transport.TSocket("localhost", 9090));
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TCompactProtocol.Factory(), transport);
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```

Keep in mind that this change might not work if the server you're connecting to doesn't support non-blocking transports. In that case, you would need to update the server code or find an alternative solution.