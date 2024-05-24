```java
@Override
public void init(OutputStream os) {
  this.os = os;
  final int bufferCapacity = 10;
  framedTransport = new org.apache.thrift.transport.layered.TFastFramedTransport(new TIOStreamTransport(os), bufferCapacity);
  protocol = new TBinaryProtocol(framedTransport);
}
```