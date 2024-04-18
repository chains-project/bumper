```java
import org.apache.thrift.transport.TFramedTransport;

public class AppenderUtils {

    public static TFramedTransport createFramedTransport(String host, int port) {
        return new TFramedTransport(new TSocket(host, port));
    }
}
```