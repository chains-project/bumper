```java
import org.apache.thrift.transport.TNonblockingTransport;

public class AppenderUtils {

    public static TNonblockingTransport createNonblockingTransport(TNonblockingTransport transport) {
        return transport;
    }
}
```