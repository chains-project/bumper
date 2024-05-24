Here is the patched code:
```
public void init(OutputStream os) {
    this.os = os;
    // Use the TFastFramedTransport to be compatible with singer_thrift log.
    final int bufferCapacity = 10;
    TIOStreamTransport ioStreamTransport = new TIOStreamTransport(os);
    TFramedTransport framedTransport = new TFramedTransport(ioStreamTransport, bufferCapacity);
    protocol = new TBinaryProtocol(framedTransport);
}
```