```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;

public class ThriftReader {
    public void read() {
        TTransport transport = new TSocket("localhost", 9090);
        TProtocol protocol = new TBinaryProtocol(transport);
        // ...
    }
}
```