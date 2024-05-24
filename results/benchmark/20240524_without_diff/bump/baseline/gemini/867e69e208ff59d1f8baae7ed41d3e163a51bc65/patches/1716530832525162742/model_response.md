```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TNonblockingTransport;

public class ThriftReader {

  public void read(TNonblockingTransport transport) {
    // Use the new TTransportFactory to create a TFramedTransport instance.
    TTransport framedTransport = new TTransportFactory().getTransport(transport);
    // Use the framedTransport to read data from the underlying transport.
    // ...
  }
}
```