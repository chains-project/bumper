```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TIOStreamTransport to be compatible with singer_thrift
    // log.
    final org.apache.thrift.TConfiguration tConfig = new org.apache.thrift.TConfiguration();
    org.apache.thrift.transport.TIOStreamTransport tIOStreamTransport = new org.apache.thrift.transport.TIOStreamTransport(tConfig, os);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(tIOStreamTransport);
}
```