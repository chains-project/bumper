```java
  import org.apache.thrift.transport.TTransport;
  import org.apache.thrift.transport.TTransportException;
  import org.apache.thrift.transport.TTransportFactory;

  // ...

  private TTransport createTransport(String host, int port, int timeout) throws TTransportException {
    // ++
    return TTransportFactory.getFramedTransport(host, port, timeout);
  }
```