```java
  public void init(OutputStream os) {
      this.os = os;
      // Use the TLayeredTransport to be compatible with singer_thrift
      // log.
      final int bufferCapacity = 10;
      framedTransport = new TLayeredTransport(new TFastFramedTransport(new TIOStreamTransport(os),
          bufferCapacity));
      protocol = new TBinaryProtocol(framedTransport);
    }
```