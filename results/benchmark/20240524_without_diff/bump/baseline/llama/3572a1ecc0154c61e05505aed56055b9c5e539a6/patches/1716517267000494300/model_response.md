Here is the patched code:
```
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;

TFramedTransport transport = new TFramedTransport(new TIOStreamTransport(new TConfiguration(), System.out));
```