```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.TConfiguration;

public TFramedTransport createTransport(TTransport transport) {
    return new TFramedTransport(transport);
}
```