```java
import org.apache.thrift.transport.TTransport;

  public class ThriftReader extends Reader<TTransport> {

    @Override
    public void start() {
      // Initialize the reader
      try {
        this.transport = new TFramedTransport(new TSocket(this.host, this.port));
        this.transport.open();
        this.protocol = new TBinaryProtocol(this.transport);
        this.client = new ThriftClient(this.protocol);
      } catch (TException e) {
        throw new RuntimeException("Failed to initialize Thrift reader", e);
      }
    }
  }
```