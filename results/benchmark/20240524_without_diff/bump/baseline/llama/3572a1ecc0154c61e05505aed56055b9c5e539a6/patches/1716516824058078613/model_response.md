```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;

TFramedTransport transport = new TFramedTransport(new TMemoryTransport(new byte[1024]));
```