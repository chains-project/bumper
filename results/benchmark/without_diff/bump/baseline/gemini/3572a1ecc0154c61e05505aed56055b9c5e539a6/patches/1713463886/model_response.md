```java
import org.apache.thrift.transport.TFramedTransport;

public class AppenderUtils {

    public static TFastFramedTransport getFastFramedTransport(String host, int port) {
        return new TFramedTransport(host, port);
    }
}
```