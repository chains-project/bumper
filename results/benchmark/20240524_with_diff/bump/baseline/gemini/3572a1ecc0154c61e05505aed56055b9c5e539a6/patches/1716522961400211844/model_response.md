```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportFactory;

public class AppenderUtils {

    public static TTransport createTransport(TTransport underlyingTransport) {
        return new TTransportFactory().getTransport(underlyingTransport);
    }
}
```