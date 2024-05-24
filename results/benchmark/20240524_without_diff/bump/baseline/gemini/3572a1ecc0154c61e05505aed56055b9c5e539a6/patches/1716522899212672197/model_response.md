```java
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

    public static TTransport createTransport(String host, int port) {
        // Use a TNonblockingSocket instead of a TFastFramedTransport
        return new TNonblockingSocket(host, port);
    }

}
```