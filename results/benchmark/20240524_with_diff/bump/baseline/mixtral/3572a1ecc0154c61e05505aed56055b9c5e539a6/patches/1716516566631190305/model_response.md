Here's the fixed version of the failing client code:
```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransportFactory;

// ...

TFastFramedTransport.Factory factory = new TFastFramedTransport.Factory();
TTransport transport = factory.getTransport(new TSocket(host, port));
TFramedTransport framedTransport = new TFramedTransport(transport);
```
The change made is to use the `TFastFramedTransport` from the `layered` package. The `TFastFramedTransport` from the `transport` package has been removed in the new version. The `TFastFramedTransport.Factory` is used to create a `TFastFramedTransport` instance.