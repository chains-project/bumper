```java
  import org.apache.thrift.transport.TFastFramedTransport;
  import org.apache.thrift.transport.TTransportFactory;

  public class AppenderUtils {
    public static TTransportFactory createTransportFactory(String host, int port, int timeout) {
      return new TFastFramedTransport.Factory();
    }
  }
```