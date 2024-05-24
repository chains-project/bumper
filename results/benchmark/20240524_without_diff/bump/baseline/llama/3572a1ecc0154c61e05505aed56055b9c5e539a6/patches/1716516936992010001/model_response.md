```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFramedTransport;

TFramedTransport transport = new TFramedTransport(new TMemoryTransport());
```