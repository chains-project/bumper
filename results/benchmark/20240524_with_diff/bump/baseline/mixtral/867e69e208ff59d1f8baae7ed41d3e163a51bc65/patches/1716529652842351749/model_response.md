Here's the fixed version of the code:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransportFactory;

TTransport transport = new TFramedTransport(new TTransportFactory().getTransport(new TSocket("localhost", 9090)));
```

Changes made:

* Imported `TTransportFactory` from `org.apache.thrift.transport` package.
* Created a `TSocket` object to specify the host and port of the Thrift service.
* Used `TTransportFactory` to get a `TTransport` instance from the `TSocket` object.
* Wrapped the `TTransport` instance with a `TFramedTransport` object.