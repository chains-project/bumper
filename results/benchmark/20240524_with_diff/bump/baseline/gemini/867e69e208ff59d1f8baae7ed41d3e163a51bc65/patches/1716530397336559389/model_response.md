```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFramedTransport;

public class SimpleThriftLogger {

  public void log(String message) {
    // Create a new TFramedTransport instance with a default buffer size.
    TTransport transport = new TFramedTransport(new TMemoryTransport());

    // Use the transport to send the message.
    // ...
  }
}
```