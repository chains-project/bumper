```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

public class ThriftReader {

    public TTransport createTransport(String host, int port) throws TTransportException {
        return new TFramedTransport(new TSocket(host, port));
    }
}
```