```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    try {
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TBinaryProtocol.Factory());
    } catch (org.apache.thrift.transport.TTransportException e) {
        return null;
    }
}
```