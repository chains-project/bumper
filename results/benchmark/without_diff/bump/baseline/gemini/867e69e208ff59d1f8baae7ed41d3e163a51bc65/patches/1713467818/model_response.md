```java
import org.apache.thrift.transport.TTransport;

import com.pinterest.singer.thrift.SingerThrift;

public class ThriftReader {

  private SingerThrift.Iface client;

  public ThriftReader(TTransport transport) {
    this.client = new SingerThrift.Client(transport);
  }

  public void read() throws Exception {
    // Read data from the Thrift server.
    client.read();
  }
}
```