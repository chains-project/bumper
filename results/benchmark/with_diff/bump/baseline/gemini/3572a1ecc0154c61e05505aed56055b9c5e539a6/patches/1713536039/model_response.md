```java
import org.apache.thrift.transport.TIOStreamTransport;

public class AppenderUtils {
  public static TIOStreamTransport createTransport(TConfiguration config, InputStream in, OutputStream out) {
    return new TIOStreamTransport(config, in, out);
  }
}
```