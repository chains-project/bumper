Here's the fixed version of the method using `TNonblockingTransport` instead of the deprecated `TFramedTransport`:

```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.transport.TTransport transport = null;
    try {
        transport = new org.apache.thrift.transport.TNonblockingTransport(new org.apache.thrift.transport.TSocket("localhost", 9090));
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TCompactProtocol.Factory(), transport);
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```