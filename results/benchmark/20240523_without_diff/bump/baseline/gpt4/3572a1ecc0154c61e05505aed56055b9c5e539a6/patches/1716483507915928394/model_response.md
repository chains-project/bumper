```java
@Override
public void init(OutputStream os) {
  this.os = os;
  final int bufferCapacity = 10;
  try {
    framedTransport = new TFastFramedTransport(new TIOStreamTransport(os), bufferCapacity);
  } catch (TTransportException e) {
    e.printStackTrace();
  }
  protocol = new TBinaryProtocol(framedTransport);
}
```