```java
import org.apache.thrift.transport.TIOStreamTransport;

public class AppenderUtils {

    public static TIOStreamTransport createTransport(String host, int port) {
        // Create a TIOStreamTransport with the specified host and port.
        return new TIOStreamTransport(null, host, port);
    }
}
```