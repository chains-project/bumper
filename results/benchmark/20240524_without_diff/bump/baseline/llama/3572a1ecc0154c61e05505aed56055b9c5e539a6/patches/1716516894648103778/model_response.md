```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;

public TFramedTransport createTransport(TTransport transport) {
    return new TFramedTransport(transport);
}
```