```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

public class SimpleThriftLogger {

    private static final TTransport transport = new TFramedTransport(null);

    public static void main(String[] args) {
        try {
            transport.open();
        } catch (TTransportException e) {
            e.printStackTrace();
        }
    }
}
```