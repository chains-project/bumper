```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFramedTransport;

public TFramedTransport transport = new TFramedTransport(new TMemoryTransport(4096));
```