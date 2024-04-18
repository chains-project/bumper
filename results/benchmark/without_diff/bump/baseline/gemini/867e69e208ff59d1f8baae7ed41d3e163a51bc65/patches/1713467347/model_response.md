```java
  import org.apache.thrift.transport.TTransport;

  public class SimpleThriftLogger {

    public static void logThriftException(TTransport transport, String message) {
      if (transport instanceof TFramedTransport) {
        // Log the exception message.
        System.err.println(message);
      } else {
        // Log the exception message and the stack trace.
        System.err.println(message);
        transport.close();
      }
    }
  }
```