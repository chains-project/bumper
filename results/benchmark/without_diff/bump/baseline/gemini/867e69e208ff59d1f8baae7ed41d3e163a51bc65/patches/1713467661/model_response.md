```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TFramedTransport;

public class ThriftReader {

    public TTransport getTransport(String host, int port) throws Exception {
        TTransport transport = new TFramedTransport(new TSocket(host, port));
        transport.open();
        return transport;
    }
}
```