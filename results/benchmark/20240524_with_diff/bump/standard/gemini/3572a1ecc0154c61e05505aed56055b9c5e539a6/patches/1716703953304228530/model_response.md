```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.TConfiguration conf = new org.apache.thrift.TConfiguration();
    org.apache.thrift.protocol.TProtocolFactory protFactory = new org.apache.thrift.protocol.TBinaryProtocol.Factory();
    return new org.apache.thrift.TDeserializer(protFactory, conf);
}
```