```
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.TConfiguration;

public TFramedTransport createFramedTransport(TTransport transport) {
    return new TFramedTransport(transport);
}
```