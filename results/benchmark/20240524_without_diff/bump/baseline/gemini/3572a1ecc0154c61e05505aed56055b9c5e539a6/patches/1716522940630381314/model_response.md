```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport;

public class AppenderUtils {

    public static TTransport createTransport(TTransport underlyingTransport) {
        return new TFastFramedTransport(underlyingTransport);
    }
}
```