```java
import org.apache.thrift.transport.TFramedTransport;

  public static void closeTransport(TFastFramedTransport transport) {
    if (transport != null) {
      try {
        transport.close();
      } catch (Exception e) {
        // Ignore the exception
      }
    }
  }
```