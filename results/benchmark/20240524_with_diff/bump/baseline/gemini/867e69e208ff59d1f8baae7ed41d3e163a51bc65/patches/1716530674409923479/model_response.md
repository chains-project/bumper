```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportFactory;

public class ThriftReader {

    public TTransport createTransport(String host, int port) {
        TTransport transport = new TSimpleFileTransport(null, "/tmp/thrift.log", true, true, true);
        return transport;
    }
}
```