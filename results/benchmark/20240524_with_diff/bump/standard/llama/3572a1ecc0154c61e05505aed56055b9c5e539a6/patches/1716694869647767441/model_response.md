```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    java.io.InputStream inputStream = new java.io.ByteArrayInputStream(new byte[0]);
    org.apache.thrift.transport.TIOStreamTransport transport = new org.apache.thrift.transport.TIOStreamTransport(new org.apache.thrift.TConfiguration(), inputStream, null);
    return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TBinaryProtocol(transport));
}
```