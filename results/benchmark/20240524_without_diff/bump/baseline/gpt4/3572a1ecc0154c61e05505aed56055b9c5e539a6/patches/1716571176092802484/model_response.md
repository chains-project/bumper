```java
@Override
public void init(OutputStream os) {
  this.os = os;
  // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
  // log.
  final int bufferCapacity = 10;
  
  TTransport tIOStreamTransport = new TIOStreamTransport(os);
  framedTransport = new TFastFramedTransport(tIOStreamTransport, bufferCapacity);
  protocol = new TBinaryProtocol(framedTransport);
}
```