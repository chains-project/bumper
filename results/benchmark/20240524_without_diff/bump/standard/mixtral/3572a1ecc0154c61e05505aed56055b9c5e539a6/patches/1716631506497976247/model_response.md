Here is the updated code that uses `TFramedTransport` from the `org.apache. thrift.transport.server` package instead of `org.apache.thrift.transport`:
```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.transport.TTransport transport = null;
    try {
        transport = new org.apache.thrift.transport.server.TFramedTransport(new org.apache.thrift.transport.TSocket("localhost", 9090));
        transport.open();
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TCompactProtocol(transport));
     } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
  } finally {
    if (transport != null) {
        transport.close();
    }
  }
}
```
This change should fix the error caused by the missing `TFramedTransport` class in the `org.apache.thrift.transport` package.