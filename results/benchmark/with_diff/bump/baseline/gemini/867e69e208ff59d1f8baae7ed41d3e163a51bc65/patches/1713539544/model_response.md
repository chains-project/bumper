```java
import org.apache.thrift.transport.TTransport;

  // -- import org.apache.thrift.transport.TFramedTransport;

  public class ThriftReader {

    // -- public ThriftReader(TFramedTransport transport) {
    public ThriftReader(TTransport transport) {
      // -- this.transport = transport;
      this.transport = transport;
    }

    // -- @Override
    public void open() throws Exception {
      transport.open();
    }

    // -- @Override
    public void close() {
      transport.close();
    }

    // -- @Override
    public TTransport getTransport() {
      return transport;
    }
  }
```