```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    try {
        org.apache.thrift.protocol.TBinaryProtocol.Factory factory = new org.apache.thrift.protocol.TBinaryProtocol.Factory();
        return new org.apache.thrift.TDeserializer(factory.getProtocol(new org.apache.thrift.transport.TIOStreamTransport(new java.io.ByteArrayOutputStream())));
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```