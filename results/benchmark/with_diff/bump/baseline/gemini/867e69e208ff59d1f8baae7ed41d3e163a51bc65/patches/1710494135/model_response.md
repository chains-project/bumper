```java
  import org.apache.thrift.transport.TFramedTransportFactory;
  import org.apache.thrift.transport.TTransport;

  ...

  TTransport transport = new TFramedTransportFactory().getTransport(socket);
```