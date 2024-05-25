```java
import org.apache.thrift.transport.TFramedTransport;

public class AppenderUtils {

    public static TFastFramedTransport createFastFramedTransport(String host, int port) {
        return new TFramedTransport(new TSocket(host, port));
    }
}
```