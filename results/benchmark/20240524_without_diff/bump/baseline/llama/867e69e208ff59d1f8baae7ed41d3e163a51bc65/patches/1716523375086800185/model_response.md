```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFramedTransport;

TTransport transport = ...; // assuming this is set elsewhere in your code
TFramedTransport framedTransport = new TFramedTransport(transport);
```