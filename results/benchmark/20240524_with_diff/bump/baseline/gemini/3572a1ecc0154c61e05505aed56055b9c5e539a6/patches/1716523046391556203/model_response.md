```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;
import org.apache.thrift.transport.layered.TFastFramedTransport;

public class AppenderUtils {

  public static TTransport createTFastFramedTransport(TTransport underlying) throws TTransportException {
    return new TFastFramedTransport(underlying);
  }
}
```