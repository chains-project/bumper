```java
import com.google.common.base.Preconditions;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.transport.TFramedTransport;

import java.util.concurrent.TimeUnit;

public class AppenderUtils {

  public static void main(String[] args) throws Exception {
    final TFramedTransport transport = new TFramedTransport(new TFastFramedTransport(null));
    final TBinaryProtocol protocol = new TBinaryProtocol(transport);
    Preconditions.checkState(protocol.getTransport() instanceof TFramedTransport);
    transport.close();
  }
}
```