```java
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

    public static TTransport getTransport(TTransport transport) {
        // Check if the transport is already a TFastFramedTransport
        if (transport instanceof TFastFramedTransport) {
            return transport;
        }

        // Wrap the transport in a TFastFramedTransport
        return new TFastFramedTransport(transport);
    }
}
```