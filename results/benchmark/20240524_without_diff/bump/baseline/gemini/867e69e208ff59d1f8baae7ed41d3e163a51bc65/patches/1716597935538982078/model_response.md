```java
import org.apache.thrift.transport.TFramedTransport;

public class ThriftReader {

    public void read(String path) throws Exception {
        TFramedTransport transport = new TFramedTransport(null);
        // Rest of the code remains the same
    }
}
```