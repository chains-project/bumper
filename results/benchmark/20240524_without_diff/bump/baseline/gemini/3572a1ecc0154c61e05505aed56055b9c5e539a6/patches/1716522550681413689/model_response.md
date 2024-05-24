```java
import org.apache.thrift.transport.TNonblockingTransport;

public class AppenderUtils {

    public static TNonblockingTransport wrapNonblockingSocket(TNonblockingTransport transport, String host, int port) {
        // Create a TFastFramedTransport around the socket transport
        return new TFastFramedTransport(transport);
    }
}
```