```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportFactory;

public class AppenderUtils {

    public static TTransport createTransport(String host, int port) {
        TTransport transport = new TSocket(host, port);
        transport = new TFramedTransport(transport);
        return transport;
    }
}
```