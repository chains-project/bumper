```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TNonblockingTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport;

public class AppenderUtils {

    public static TNonblockingTransport createNonblockingTransport(TTransport underlyingTransport) {
        return new TNonblockingTransport(underlyingTransport);
    }

    public static TFastFramedTransport createFastFramedTransport(TNonblockingTransport underlyingTransport) {
        return new TFastFramedTransport(underlyingTransport);
    }
}
```