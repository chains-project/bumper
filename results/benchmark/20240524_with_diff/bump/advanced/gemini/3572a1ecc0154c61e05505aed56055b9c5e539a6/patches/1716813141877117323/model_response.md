```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.TConfiguration tConfiguration = new org.apache.thrift.TConfiguration();
    java.io.ByteArrayInputStream byteArrayInputStream = new java.io.ByteArrayInputStream(new byte[0]);
    java.io.ByteArrayOutputStream byteArrayOutputStream = new java.io.ByteArrayOutputStream();
    return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TBinaryProtocol.Factory(), new org.apache.thrift.transport.TIOStreamTransport(tConfiguration, byteArrayInputStream, byteArrayOutputStream));
}
```