```java
public void init(OutputStream os) {
    this.os = os;
    final int bufferCapacity = 10;
    TIOStreamTransport tioStreamTransport = new TIOStreamTransport(os);
    TFramedTransport framedTransport = new TFramedTransport(tioStreamTransport, bufferCapacity);
    protocol = new TBinaryProtocol(framedTransport);
}
```