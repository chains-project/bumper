```java
import org.apache.thrift.transport.TTransportFactory;
import org.apache.thrift.transport.layered.TFramedTransport;

TFramedTransport transport = new TFramedTransport(TTransportFactory.getTransport(new TMemoryTransport(1024)));
```