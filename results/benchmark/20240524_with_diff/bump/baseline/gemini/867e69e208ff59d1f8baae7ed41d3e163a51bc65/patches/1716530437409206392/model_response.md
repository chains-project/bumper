```java
  import org.apache.thrift.TConfiguration;
  import org.apache.thrift.transport.TNonblockingTransport;
  import org.apache.thrift.transport.TTransport;
  import org.apache.thrift.transport.TFramedTransport;

  public class SimpleThriftLogger {

    public static void main(String[] args) {
      // Create a non-blocking transport
      TNonblockingTransport transport = new TNonblockingTransport(new TConfiguration());

      // Wrap the transport in a framed transport
      TTransport framedTransport = new TFramedTransport(transport);

      // Use the framed transport to send and receive data
      // ...
    }
  }
```