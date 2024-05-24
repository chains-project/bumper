Here's the proposed patch:
```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransportFactory;

public class SimpleThriftLogger {
    // ...

    private static TFramedTransport createFramedTransport(TTransport transport) {
        return new TFramedTransport(transport);
    }

    // ...
}
```
In the new library version, `TFramedTransport` constructor now requires a `TTransport` argument. To fix the issue, we create a new method `createFramedTransport` that takes a `TTransport` instance and returns a new `TFramedTransport` instance initialized with the provided transport. We then use this method to create the framed transport instance.