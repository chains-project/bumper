```java
import org.apache.thrift.transport.TTransport;

public class SimpleThriftLogger {

    private TTransport transport;

    public SimpleThriftLogger(TTransport transport) {
        this.transport = transport;
    }

    public void log(String message) {
        try {
            transport.write(message.getBytes());
            transport.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```