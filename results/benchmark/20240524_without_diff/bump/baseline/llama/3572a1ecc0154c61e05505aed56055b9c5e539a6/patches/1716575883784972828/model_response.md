```java
public void init(OutputStream os) {
  this.os = os;
  final int bufferCapacity = 10;
  framedTransport = new TFramedTransport(new TIOStreamTransport(os));
  protocol = new TBinaryProtocol(framedTransport);
}
```