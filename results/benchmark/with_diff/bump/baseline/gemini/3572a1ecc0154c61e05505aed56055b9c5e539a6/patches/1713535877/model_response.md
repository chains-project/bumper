```java
import org.apache.thrift.TConfiguration;
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

    public static TTransport createTransport(TConfiguration config, InputStream in, OutputStream out) {
        return new TIOStreamTransport(config, in, out);
    }
}
```