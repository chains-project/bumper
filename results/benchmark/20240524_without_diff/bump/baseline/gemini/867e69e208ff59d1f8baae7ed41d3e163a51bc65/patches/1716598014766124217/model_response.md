```java
import org.apache.thrift.transport.TFramedTransport;

public class ThriftReader {

    public TFramedTransport createTransport(String host, int port) {
        return new TFramedTransport(new TSocket(host, port));
    }
}
```