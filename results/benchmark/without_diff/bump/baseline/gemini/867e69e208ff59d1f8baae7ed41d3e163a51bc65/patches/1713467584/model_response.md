```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TFramedTransport;

public class ThriftReader {

  public TTransport createTransport(String host, int port) {
    TTransport transport = new TSocket(host, port);
    return new TFramedTransport(transport);
  }
}
```