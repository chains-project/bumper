Here's the proposed patch for the failing client code:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport;
import org.apache.thrift.transport.layered.TFastFramedTransport$Factory;

TTransport transport = new TFastFramedTransport.Factory().getTransport(new TFramedTransport.Factory().getTransport(new TTransportFactory().getTransport(new TSocket("localhost", 9090))));
```

This code creates a TFramedTransport by using the TFastFramedTransport$Factory to get a TTransport, which is then passed to the TFramedTransport$Factory to get a TFramedTransport. This is then passed to the TSocket constructor to create a TSocket transport. This code should work with the new library version.