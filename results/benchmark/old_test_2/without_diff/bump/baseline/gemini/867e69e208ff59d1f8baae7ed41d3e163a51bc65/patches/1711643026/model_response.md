```java
  import org.apache.thrift.transport.TTransport;
  import org.apache.thrift.transport.TTransportFactory;

  public class ThriftReader {

    private final TTransportFactory transportFactory;

    public ThriftReader(TTransportFactory transportFactory) {
      this.transportFactory = transportFactory;
    }

    public TTransport openTransport() {
      TTransport transport = transportFactory.getTransport();
      if (transport instanceof TFramedTransport) {
        ((TFramedTransport) transport).open();
      } else {
        transport.open();
      }
      return transport;
    }
  }
```