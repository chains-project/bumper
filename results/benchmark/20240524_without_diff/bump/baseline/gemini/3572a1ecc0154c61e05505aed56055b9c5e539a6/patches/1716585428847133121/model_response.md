```java
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

    public static TTransport createTransport(String host, int port) {
        return new TFastFramedTransport(host, port);
    }
}
```