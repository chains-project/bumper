```java
public void init(OutputStream os) {
  this.os = os;
  final int bufferCapacity = 10;
  TIOStreamTransport tioStreamTransport = new TIOStreamTransport(new TConfiguration(), os);
  framedTransport = new TFastFramedTransport.Factory().getTransport(tioStreamTransport);
  protocol = new TBinaryProtocol(framedTransport);
}
```