```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    try {
        java.io.ByteArrayInputStream inputStream = new java.io.ByteArrayInputStream(new byte[0]);
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TBinaryProtocol(new org.apache.thrift.transport.TIOStreamTransport(new org.apache.thrift.TConfiguration(), inputStream)));
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```