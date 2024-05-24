```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportFactory;

public class ThriftReader {

  public ThriftReader(TTransport transport) {
    // Create a new TTransportFactory that uses the TFramedTransport class.
    TTransportFactory transportFactory = new TTransportFactory() {
      @Override
      public TTransport getTransport(TTransport base) {
        return new TFramedTransport(base);
      }
    };

    // Wrap the original transport with the new transport factory.
    transport = transportFactory.getTransport(transport);
  }
}
```