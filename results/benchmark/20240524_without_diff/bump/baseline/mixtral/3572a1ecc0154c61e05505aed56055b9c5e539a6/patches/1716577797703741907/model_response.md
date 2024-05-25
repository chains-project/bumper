Here's a possible patch to fix the issue:

```java
  @Override
  public void init(OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    TTransport transport = new TFramedTransport(new TIOStreamTransport(os), bufferCapacity);
    TProtocolFactory protocolFactory = new TBinaryProtocol.Factory();
    framedTransport = (TFramedTransport) transport;
    protocol = protocolFactory.getProtocol(transport);
  }
```

Note that I had to cast the `transport` to `TFramedTransport` because the `framedTransport` variable is declared as such. Also, I used a `TProtocolFactory` to create the `protocol` object, since the `TBinaryProtocol` constructor that takes a `TTransport` as argument is not available anymore.