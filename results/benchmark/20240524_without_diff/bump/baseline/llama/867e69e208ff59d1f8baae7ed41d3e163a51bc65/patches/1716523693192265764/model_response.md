```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFramedTransport;

TTransport transport = ...; // Initialize your transport
TFramedTransport framedTransport = new TFramedTransport(transport);
```