```java
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

    public static TTransport createTransport(String host, int port) {
        // Use the new TEndpointTransport class instead of the removed TFastFramedTransport class.
        return new TEndpointTransport(host, port);
    }
}
```