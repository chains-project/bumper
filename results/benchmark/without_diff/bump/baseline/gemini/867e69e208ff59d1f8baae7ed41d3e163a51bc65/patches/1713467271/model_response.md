```java
import org.apache.thrift.transport.TFramedTransport;

public class SimpleThriftLogger {

    private static final TFramedTransport transport = new TFramedTransport(null);

    public static void log(String message) {
        try {
            transport.write(message.getBytes());
            transport.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```