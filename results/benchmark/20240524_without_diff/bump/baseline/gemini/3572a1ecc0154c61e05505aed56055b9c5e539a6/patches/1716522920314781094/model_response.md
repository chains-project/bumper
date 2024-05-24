```java
import org.apache.thrift.transport.TTransport;

public class AppenderUtils {

  public static TTransport createTransport(String host, int port) {
    // Use TFastFramedTransport instead of the removed TFramedTransport
    return new org.apache.thrift.transport.TFastFramedTransport(new org.apache.thrift.transport.TSocket(host, port));
  }
}
```