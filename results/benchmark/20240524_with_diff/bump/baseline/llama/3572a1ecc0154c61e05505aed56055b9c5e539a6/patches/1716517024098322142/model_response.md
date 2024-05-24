```
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TConfiguration;

TFramedTransport transport = new TFramedTransport(new TConfiguration(), new TMemoryTransport(new byte[0]));
```