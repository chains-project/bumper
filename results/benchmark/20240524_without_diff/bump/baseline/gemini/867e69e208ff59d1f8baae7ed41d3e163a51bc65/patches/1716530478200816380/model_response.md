```java
import org.apache.thrift.transport.TTransport;

public class SimpleThriftLogger {

  public static void main(String[] args) {
    // Create a TTransport object using the appropriate factory method.
    TTransport transport = new TFramedTransport(new TSocket("localhost", 9090));
    // Open the transport.
    transport.open();
    // ...
  }
}
```