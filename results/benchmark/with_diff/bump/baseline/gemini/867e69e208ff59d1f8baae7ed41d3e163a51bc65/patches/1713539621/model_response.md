```java
import org.apache.thrift.transport.TTransport;

public class ThriftReader {

    public TTransport createTransport(String host, int port) {
        // Use a different transport implementation that is available in the new library version
        return new TSocket(host, port);
    }
}
```