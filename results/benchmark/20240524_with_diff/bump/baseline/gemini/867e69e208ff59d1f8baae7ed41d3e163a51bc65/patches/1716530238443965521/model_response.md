```java
import org.apache.thrift.transport.TConfiguration;
import org.apache.thrift.transport.TEndpointTransport;

public class SimpleThriftLogger {

    public void log(String message) {
        TConfiguration config = new TConfiguration();
        TEndpointTransport transport = new TEndpointTransport(config);
        // Use the transport to send the log message
        // ...
    }
}
```