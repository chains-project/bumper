```java
public void init(OutputStream os) {
    this.os = os;
    final int bufferCapacity = 10;
    TIOStreamTransport tIOStreamTransport = new TIOStreamTransport(os);
    TFastFramedTransport framedTransport = new TFastFramedTransport(tIOStreamTransport, bufferCapacity);
    protocol = new TBinaryProtocol(framedTransport);
}
```