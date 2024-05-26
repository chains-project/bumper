Here'Summary of the changes:

- Replace `TFastFramedTransport` with `TFramedTransport` from the `org.apache.thrift.transport` package.
- Update the package name for `TIOStreamTransport` to `org.apache.thrift.transport.TIOStreamTransport`.

Updated client code:
```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os), bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(frateDTransport);
}
```