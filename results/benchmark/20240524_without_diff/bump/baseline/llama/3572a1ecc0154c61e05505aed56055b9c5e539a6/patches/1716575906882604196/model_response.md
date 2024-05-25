```java
public void init(OutputStream os) {
  this.os = os;
  // Use the TSimpleFileTransport to be compatible with singer_thrift log.
  framedTransport = new TIOStreamTransport(os);
  protocol = new TBinaryProtocol(framedTransport);
}
```