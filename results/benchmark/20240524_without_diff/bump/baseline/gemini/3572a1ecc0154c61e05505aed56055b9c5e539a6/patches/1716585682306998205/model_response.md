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
      // Add a flusher to the transport to ensure messages are flushed to the
      // underlying stream.
      framedTransport.setFlusher(new TFlushingTransport(framedTransport));
    }
```