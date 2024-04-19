```java
  import org.apache.thrift.transport.TIOStreamTransport;
  import org.apache.thrift.TConfiguration;
  import java.io.InputStream;
  import java.io.OutputStream;

  public class AppenderUtils {

    public static TIOStreamTransport createTransport(InputStream in, OutputStream out, TConfiguration configuration) {
      return new TIOStreamTransport(configuration, in, out);
    }
  }
```