```java
public void init(OutputStream os) {
  this.os = os;
  final int bufferCapacity = 10;
  TTransport transport = new TIOStreamTransport(os);
  transport.open();
  framedTransport = new TFramedTransport(transport);
  protocol = new TBinaryProtocol(framedTransport);
}
```