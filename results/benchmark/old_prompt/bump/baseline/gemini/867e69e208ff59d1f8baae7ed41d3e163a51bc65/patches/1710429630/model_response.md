```java
  import org.apache.thrift.transport.TTransport;
  import org.apache.thrift.transport.TTransportFactory;

  private static TTransportFactory transportFactory = new TTransportFactory() {
    @Override
    public TTransport getTransport(TTransport trans) {
      return new TFramedTransport(trans);
    }
  };
```