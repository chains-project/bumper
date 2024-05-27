```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.protocol.TProtocolFactory factory = new org.apache.thrift.protocol.TBinaryProtocol.Factory();
    return new org.apache.thrift.TDeserializer(factory);
}
```