```java
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

    public static TTransport wrapTransport(TTransport transport) {
        return transport;
    }
}
```