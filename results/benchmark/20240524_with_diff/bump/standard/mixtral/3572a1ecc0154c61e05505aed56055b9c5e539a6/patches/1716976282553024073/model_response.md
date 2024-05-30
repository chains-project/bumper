Here's a patch that you can apply to the failing client code:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFastFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os));
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
    framedTransport.set FramedTransportEventListener(new org.apache.thrift.transport.FramedTransport.FramedTransportEventListener() {
        @Override
        public void frameRead(int length) {}

        @Override
        public void frameWritten(int length) {}
    });
    framedTransport.open();
}
```

In this patch, I replaced the `TFastFramedTransport` with `TFastFramedTransport` which is still available in the new library version. Also, I added the `FramedTransportEventListener` to the `TFastFramedTransport` to avoid any potential issues.