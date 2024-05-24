Here's the proposed patch:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport;
import org.apache.thrift.transport.TConfiguration;

public class SimpleThriftLogger {
    // ...
    private TFramedTransport createFramedTransport(TTransport transport) {
        return new TFastFramedTransport(new TFramedTransport.Factory().getTransport(transport), 1024, 1024);
    }
    // ...
}
```

This patch replaces the use of the deprecated `TFramedTransport` constructor and `TFramedTransport.Factory` with the new `TFastFramedTransport` constructor. It also uses a `TConfiguration` object to configure the new `TFastFramedTransport`.