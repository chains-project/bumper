```java
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

    public static TTransport createFramedTransport(TTransport transport) {
        return new TFastFramedTransport(transport);
    }
}
```