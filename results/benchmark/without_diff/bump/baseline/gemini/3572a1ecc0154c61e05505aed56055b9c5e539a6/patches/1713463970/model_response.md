```java
  import org.apache.thrift.transport.TTransport;
  import org.apache.thrift.transport.TFramedTransport;

  public class AppenderUtils {

    public static TTransport createTransport(String host, int port) {
      return new TFramedTransport(new TFastFramedTransport(new TSocket(host, port)));
    }
  }
```