```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

public class ThriftReader {

  private TTransport transport;

  public ThriftReader(TTransport transport) {
    this.transport = transport;
  }

  public void open() throws TTransportException {
    transport.open();
  }

  public void close() throws TTransportException {
    transport.close();
  }

  public void read(byte[] buffer) throws TTransportException {
    transport.read(buffer, 0, buffer.length);
  }
}
```