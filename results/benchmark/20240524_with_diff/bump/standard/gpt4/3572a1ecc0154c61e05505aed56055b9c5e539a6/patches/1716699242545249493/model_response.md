```java
@java.lang.Override
protected org.apache.thrift.TSerializer initialValue() {
    try {
        return new org.apache.thrift.TSerializer(new org.apache.thrift.protocol.TBinaryProtocol.Factory());
    } catch (org.apache.thrift.transport.TTransportException e) {
        return null;
    }
}
```