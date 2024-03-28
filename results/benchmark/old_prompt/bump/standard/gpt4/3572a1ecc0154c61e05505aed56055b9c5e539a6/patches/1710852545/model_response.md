```java
@java.lang.Override
protected org.apache.thrift.TSerializer initialValue() {
    org.apache.thrift.TSerializer tSerializer = null;
    try {
        tSerializer = new org.apache.thrift.TSerializer(new org.apache.thrift.protocol.TCompactProtocol.Factory());
    } catch (org.apache.thrift.transport.TTransportException e) {
        e.printStackTrace();
    }
    return tSerializer;
}
```