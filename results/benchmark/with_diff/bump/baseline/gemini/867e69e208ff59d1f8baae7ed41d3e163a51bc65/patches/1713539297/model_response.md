```java
import org.apache.thrift.transport.TTransport;

public class SimpleThriftLogger {

    private final TTransport transport;

    public SimpleThriftLogger(TTransport transport) {
        this.transport = transport;
    }

    // Override
    public void log(String message) {
        try {
            transport.write(message.getBytes());
            transport.flush();
        } catch (Exception e) {
            // Log the error message
        }
    }
}
```