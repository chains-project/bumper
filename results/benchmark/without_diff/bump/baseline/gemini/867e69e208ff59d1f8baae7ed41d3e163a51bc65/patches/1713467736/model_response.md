```java
import org.apache.thrift.transport.TFramedTransport;

public class ThriftReader {

    public ThriftReader(TFramedTransport transport) {
        this.transport = transport;
    }

    private final TFramedTransport transport;

    public void read() throws Exception {
        // Read data from the transport
        byte[] data = transport.readFrame();

        // Process the data
        // ...
    }
}
```