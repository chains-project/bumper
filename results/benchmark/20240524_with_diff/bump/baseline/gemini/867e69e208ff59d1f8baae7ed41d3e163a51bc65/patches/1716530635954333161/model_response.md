```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportFactory;

public class ThriftReader {

  public TTransport getTransport(String host, int port) {
    TTransport transport = new TSocket(host, port);
    // Use TFramedTransport instead of the removed TFramedTransportFactory
    return new TFramedTransport(transport);
  }
}
```