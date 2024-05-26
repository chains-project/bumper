```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    try {
        org.apache.thrift.protocol.TProtocol protocol = new org.apache.thrift.protocol.TBinaryProtocol(new org.apache.thrift.transport.TIOStreamTransport(new java.io.ByteArrayInputStream(new byte[0])));
        return new org.apache.thrift.TDeserializer(protocol);
    } catch (org.apache.thrift.TException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```