```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    try {
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TBinaryProtocol.Factory().getProtocol(new org.apache.thrift.transport.TIOStreamTransport(new java.io.ByteArrayInputStream(new byte[0]))));
    } catch (org.apache.thrift.TException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```