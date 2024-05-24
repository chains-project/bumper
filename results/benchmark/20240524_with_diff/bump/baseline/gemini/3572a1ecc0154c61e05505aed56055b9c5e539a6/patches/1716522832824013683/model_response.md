```java
  public void init(OutputStream os) {
      this.os = os;
      // Use the TFastFramedTransport to be compatible with singer_thrift
      // log.
      final int bufferCapacity = 10;
      // Use the TFastFramedTransport from the layered library to be compatible with the new version of the library
      framedTransport = new org.apache.thrift.transport.layered.TFastFramedTransport(new TIOStreamTransport(os),
          bufferCapacity);
      protocol = new TBinaryProtocol(framedTransport);
    }
```