```java
import org.apache.thrift.transport.TIOStreamTransport;

public class AppenderUtils {
    public static TIOStreamTransport createTransport(TConfiguration configuration) {
        return new TIOStreamTransport(configuration);
    }
}
```