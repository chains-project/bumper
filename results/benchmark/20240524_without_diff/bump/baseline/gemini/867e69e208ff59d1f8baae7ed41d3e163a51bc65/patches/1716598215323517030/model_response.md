```java
import org.apache.thrift.transport.TTransport;

public class ThriftReader {

    public TTransport getTransport(String host, int port) throws Exception {
        TTransport transport = new TFramedTransport(new TSocket(host, port));
        transport.open();
        return transport;
    }
}
```