```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport$Factory;

public class AppenderUtils {

  public static TTransport createTransport(TTransport transport) {
    return new TFastFramedTransport(transport);
  }
}
```