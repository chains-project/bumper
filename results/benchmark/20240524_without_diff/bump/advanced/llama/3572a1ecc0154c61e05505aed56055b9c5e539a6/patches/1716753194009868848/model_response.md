```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    try {
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TBinaryProtocol(new org.apache.thrift.transport.TIOStreamTransport(new java.io.ByteArrayOutputStream())));
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```