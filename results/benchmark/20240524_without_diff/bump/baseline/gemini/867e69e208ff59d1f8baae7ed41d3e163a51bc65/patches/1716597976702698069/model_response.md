```java
import org.apache.thrift.transport.TTransport;

  public class ThriftReader {

    public TTransport getTransport(String host, int port) throws Exception {
      return new TFramedTransport(new TSocket(host, port));
    }
  }
```