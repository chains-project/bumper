```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFramedTransport;

TTransport transport = ...
TFramedTransport framedTransport = new TFramedTransport(transport);
```