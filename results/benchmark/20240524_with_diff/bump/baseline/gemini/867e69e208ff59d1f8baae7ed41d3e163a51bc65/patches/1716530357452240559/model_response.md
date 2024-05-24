```java
import org.apache.thrift.transport.TTransport;

public class SimpleThriftLogger {

  public static void main(String[] args) throws Exception {
    // Create a TTransport instance using the new library version.
    TTransport transport = new TFramedTransport(new TSocket("localhost", 9090));

    // Use the transport instance as before.
    // ...
  }
}
```