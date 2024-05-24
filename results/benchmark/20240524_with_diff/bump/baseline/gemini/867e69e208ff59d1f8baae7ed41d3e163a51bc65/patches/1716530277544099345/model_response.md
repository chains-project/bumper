```java
import org.apache.thrift.transport.TTransportFactory;
import org.apache.thrift.transport.layered.TFastFramedTransport$Factory;

public class SimpleThriftLogger {

  private static final TTransportFactory transportFactory = new TFastFramedTransport$Factory();

  // ...
}
```