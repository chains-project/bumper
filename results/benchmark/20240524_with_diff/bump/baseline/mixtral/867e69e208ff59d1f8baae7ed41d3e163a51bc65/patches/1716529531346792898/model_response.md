Here's the proposed patch:
```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransportFactory;

TTransport transport = new TFramedTransport(new TTransportFactory().getTransport(new TSocket("localhost", 9090)));
```
In this patch, we're using the new `TFramedTransport` constructor that takes a `TTransport` as a parameter. We're creating a new `TSocket` and passing it to a new `TTransportFactory` to get a `TTransport`. This new `TTransport` is then passed to the `TFramedTransport` constructor. Note that we're using the new `TTransportFactory` methods added in the new library version to get a `TTransport`.