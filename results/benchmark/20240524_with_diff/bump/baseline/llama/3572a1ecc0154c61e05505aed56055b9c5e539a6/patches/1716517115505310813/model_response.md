Here is the patched code:
```java
public void init(OutputStream os) {
  this.os = os;
  // Use the TIOStreamTransport to be compatible with singer_thrift log.
  final int bufferCapacity = 10;
  TIOStreamTransport transport = new TIOStreamTransport(os);
  framedTransport = new TFastFramedTransport(transport, bufferCapacity);
  protocol = new TBinaryProtocol(framedTransport);
}
```