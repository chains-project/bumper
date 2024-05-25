```java
  import org.apache.thrift.transport.TTransport;

  public class ThriftReader {

    public TTransport createTransport(String host, int port, int timeout) throws Exception {
      return new TFramedTransport(host, port, timeout);
    }
  }
```