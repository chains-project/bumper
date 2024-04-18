```java
import org.apache.thrift.transport.TTransport;

public class ThriftReader {

    private final TTransport transport;

    public ThriftReader(TTransport transport) {
        this.transport = transport;
    }

    public void read() throws Exception {
        transport.open();
        // Read data from the transport
        transport.close();
    }
}
```