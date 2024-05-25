```java
  @Override
    public void init(OutputStream os) throws TTransportException {
      this.os = os;
      // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
      // log.
      final int bufferCapacity = 10;
      framedTransport = new TFastFramedTransport(new TIOStreamTransport(os),
          bufferCapacity);
      protocol = new TBinaryProtocol(framedTransport);
      framedTransport.open();
    }
```