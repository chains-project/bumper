```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    final int bufferCapacity = 10;
    org.apache.thrift.transport.layered.TFastFramedTransport$Factory factory = new org.apache.thrift.transport.layered.TFastFramedTransport$Factory(bufferCapacity);
    framedTransport = factory.getTransport(new org.apache.thrift.transport.TIOStreamTransport(os));
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}
```