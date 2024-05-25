```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TFramedTransport;

public class ThriftReader {

  private TTransport transport;

  public ThriftReader(TTransport transport) {
    this.transport = transport;
  }

  public void read() throws Exception {
    if (transport instanceof TFramedTransport) {
      ((TFramedTransport) transport).readFrame();
    } else {
      // Handle other transport types
    }
  }
}
```