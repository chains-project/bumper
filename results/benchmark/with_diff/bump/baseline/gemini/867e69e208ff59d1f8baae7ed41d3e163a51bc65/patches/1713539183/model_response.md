```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportFactory;

import com.pinterest.singer.utils.SimpleThriftLogger;

public class SimpleThriftLogger {

    private final TTransport transport;

    public SimpleThriftLogger(TTransport transport) {
        this.transport = transport;
    }

    public static SimpleThriftLogger create(TTransportFactory transportFactory, String host, int port) {
        TTransport transport = transportFactory.getTransport(host, port);
        return new SimpleThriftLogger(transport);
    }

    public void log(String message) {
        try {
            transport.open();
            // ++ Log message using the transport
            transport.write(message.getBytes());
            transport.flush();
        } catch (Exception e) {
            // Handle exception
        } finally {
            transport.close();
        }
    }
}
```