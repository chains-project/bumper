```java
  import org.apache.thrift.transport.TFastFramedTransport;
  import org.apache.thrift.transport.TTransport;

  public class AppenderUtils {

    public static TTransport createThriftTransport(String host, int port, int timeout) {
      return new TFastFramedTransport(new TSocket(host, port, timeout));
    }
  }
```