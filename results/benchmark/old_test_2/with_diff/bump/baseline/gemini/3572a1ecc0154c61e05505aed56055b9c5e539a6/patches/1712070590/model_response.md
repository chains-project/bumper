```java
  import org.apache.thrift.transport.TIOStreamTransport;

  ...

  TIOStreamTransport transport = new TIOStreamTransport(new TConfiguration(), out);
  TFastFramedTransport fastFramedTransport = new TFastFramedTransport(transport);
```