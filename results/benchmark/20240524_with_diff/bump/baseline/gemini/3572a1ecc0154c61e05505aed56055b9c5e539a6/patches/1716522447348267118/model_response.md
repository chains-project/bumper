```java
import org.apache.thrift.transport.TNonblockingTransport;
import org.apache.thrift.transport.TSaslClientTransport;
import org.apache.thrift.transport.TSaslServerTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport;

public class AppenderUtils {

    public static TTransport createTransport(TTransport transport, String host, int port) {
        if (transport instanceof TNonblockingTransport) {
            return new TSaslClientTransport((TNonblockingTransport) transport, host, port, null, null);
        } else if (transport instanceof TSaslServerTransport) {
            return ((TSaslServerTransport) transport).getUnderlyingTransport();
        } else {
            return new TFastFramedTransport(transport);
        }
    }
}
```