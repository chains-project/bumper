```java
  import org.apache.thrift.transport.TFastFramedTransport;

  import java.io.IOException;

  public class AppenderUtils {

    public static TFastFramedTransport createTransport(String host, int port) throws IOException {
      return new TFastFramedTransport(host, port);
    }
  }
```