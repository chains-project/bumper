```java
import org.apache.thrift.transport.TTransport;

public class ThriftReader {

    public TTransport createTransport() {
        return new TFramedTransport(null);
    }
}
```