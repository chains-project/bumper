```java
  import org.apache.thrift.transport.TFastFramedTransport;
  import org.apache.thrift.transport.TTransport;
  import org.apache.thrift.transport.TTransportFactory;

  public class AppenderUtils {

    public static TTransport createFramedTransport(TTransport transport) {
      return new TFastFramedTransport(transport);
    }

    public static TTransportFactory createFramedTransportFactory() {
      return new TTransportFactory() {
        @Override
        public TTransport getTransport(TTransport trans) {
          return createFramedTransport(trans);
        }
      };
    }
  }
```