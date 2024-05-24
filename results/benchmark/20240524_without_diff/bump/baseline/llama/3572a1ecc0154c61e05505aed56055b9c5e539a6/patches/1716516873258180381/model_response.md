```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport;

TFastFramedTransport transport = new TFastFramedTransport(new TMemoryTransport(new byte[1024]));
```