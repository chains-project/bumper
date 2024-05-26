```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    TTransport transport = new TIOStreamTransport(new ByteArrayOutputStream());
    return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TCompactProtocol.Factory(), transport);
}
```