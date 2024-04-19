Here's a proposed patch to fix the error:
```
import org.apache.thrift.transport.TTransport;

public class SimpleThriftLogger {
    private TTransport transport;

    public SimpleThriftLogger(TTransport transport) {
        this.transport = transport;
    }

    public void log(String message) {
        transport.write(message.getBytes());
    }
}
```
The patch removes the import of `TFramedTransport` and replaces it with `TTransport`. It also removes the parameter `TFramedTransport` from the constructor and replaces it with `TTransport`.

The error was caused by the removal of `TFramedTransport` in the new library version, and this patch fixes it by using the updated `TTransport` class.