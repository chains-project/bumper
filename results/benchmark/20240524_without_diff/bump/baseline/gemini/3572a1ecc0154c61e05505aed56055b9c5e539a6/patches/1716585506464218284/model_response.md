```java
  @Override
    public void init(OutputStream os) {
      this.os = os;
      // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
      // log.
      final int bufferCapacity = 10;
      framedTransport = new TFastFramedTransport(new TIOStreamTransport(os),
          bufferCapacity);
      protocol = new TBinaryProtocol(framedTransport);
      // Create a new instance of TFlushingFastFramedTransport
      final TFlushingFastFramedTransport flushingTransport = new TFlushingFastFramedTransport(framedTransport);
      // Create a new instance of TBinaryProtocol with the flushingTransport
      protocol = new TBinaryProtocol(flushingTransport);
    }
```