```java
import org.apache.thrift.transport.TTransport;

public class ThriftReader {

    public TTransport createTransport(String host, int port) {
        // Use TSocket instead of TFramedTransport to avoid the dependency on TFramedTransport
        return new TSocket(host, port);
    }
}
```