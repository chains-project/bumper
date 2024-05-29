Here is a fixed version of your code that replaces the `TFramedTransport` with `TNonblockingServerTransport` which is a part of the same package and should work as a drop-in replacement:
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
This code should be compatible with the previous version and should not require any additional changes.