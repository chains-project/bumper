```java
import org.apache.thrift.transport.TNonblockingTransport;
import org.apache.thrift.transport.TFramedTransport;

public class ThriftReader {

    private TNonblockingTransport transport;

    public ThriftReader(TNonblockingTransport transport) {
        this.transport = transport;
    }

    public void read() throws Exception {
        // Create a framed transport around the non-blocking transport.
        TFramedTransport framedTransport = new TFramedTransport(transport);

        // Read data from the framed transport.
        // ...
    }
}
```