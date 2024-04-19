```java
import org.apache.thrift.transport.TIOStreamTransport;

public class AppenderUtils {

    public static TIOStreamTransport createTransport(TConfiguration conf, InputStream in, OutputStream out) {
        return new TIOStreamTransport(conf, in, out);
    }
}
```