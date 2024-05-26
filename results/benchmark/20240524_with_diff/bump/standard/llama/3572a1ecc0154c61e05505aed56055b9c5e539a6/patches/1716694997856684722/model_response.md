```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    java.io.InputStream inputStream = new java.io.ByteArrayInputStream(new byte[0]);
    org.apache.thrift.transport.TIOStreamTransport transport = new org.apache.thrift.transport.TIOStreamTransport(new org.apache.thrift.TConfiguration(), inputStream, null);
    org.apache.thrift.protocol.TProtocolFactory protocolFactory = new org.apache.thrift.protocol.TBinaryProtocol.Factory();
    return new org.apache.thrift.TDeserializer(protocolFactory.getProtocol(transport));
}
```