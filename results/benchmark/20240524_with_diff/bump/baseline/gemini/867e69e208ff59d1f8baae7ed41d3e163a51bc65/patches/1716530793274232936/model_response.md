```java
import org.apache.thrift.TConfiguration;
import org.apache.thrift.transport.TTransport;

public class ThriftReader {

    public void read(TConfiguration configuration, TTransport transport) throws Exception {
        // Use TEndpointTransport instead of TFramedTransport
        TEndpointTransport endpointTransport = new TEndpointTransport(configuration);
        endpointTransport.setUnderlyingTransport(transport);

        // Rest of the code remains the same
        // ...
    }
}
```