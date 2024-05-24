```java
import org.apache.thrift.transport.TIOStreamTransport;

public class SimpleThriftLogger {

    public void log(String message) {
        try (TIOStreamTransport transport = new TIOStreamTransport(System.out)) {
            transport.write(message.getBytes());
            transport.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```