```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    try {
        org.apache.thrift.protocol.TProtocolFactory factory = new org.apache.thrift.protocol.TBinaryProtocol.Factory();
        org.apache.thrift.transport.TTransport transport = new org.apache.thrift.transport.TIOStreamTransport(new java.io.ByteArrayOutputStream());
        return new org.apache.thrift.TDeserializer(factory.getProtocol(transport));
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```