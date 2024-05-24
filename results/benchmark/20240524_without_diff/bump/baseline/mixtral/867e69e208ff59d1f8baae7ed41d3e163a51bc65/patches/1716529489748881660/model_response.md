Here's a possible patch to fix the error:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportFactory;

// ...

TTransport transport = new TFramedTransport(new TTransportFactory().getTransport(new TSocket("localhost", 9090)));
```

This patch creates a new `TFramedTransport` using the `TSocket` and `TTransportFactory` classes. The `TSocket` constructor takes a host and port as arguments, which should be set to the appropriate values for your use case. The `TTransportFactory` is used to create a `TTransport` instance, which is then passed to the `TFramedTransport` constructor. This should fix the "cannot find symbol" error for `TFramedTransport`.