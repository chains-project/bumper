Here's the proposed patch:

```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TFramedTransport;

public class SimpleThriftLogger {
    // ...

    @Override
    public void log(TTransport transport) {
        TFramedTransport framedTransport = (transport instanceof TFramedTransport)
                ? (TFramedTransport) transport
                : new TFramedTransport(transport);

        // ...
    }

    // ...
}
```

This patch checks if the given `transport` is an instance of `TFramedTransport` and if not, it creates a new `TFramedTransport` wrapper around it. This way, the code should work even if the external dependency update removed the `TFramedTransport` class.