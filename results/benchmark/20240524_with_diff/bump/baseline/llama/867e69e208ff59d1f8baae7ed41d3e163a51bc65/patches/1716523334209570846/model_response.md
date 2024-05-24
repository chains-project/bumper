```
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFramedTransport;

TTransport transport = new TFramedTransport(new TMemoryInputTransport(new byte[0]));
```