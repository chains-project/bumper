```java
  import org.apache.thrift.transport.TTransport;

  public void log(String message, TTransport transport) {
    if (transport instanceof TFramedTransport) {
      // Log the message using the TFramedTransport
      // ...
    } else {
      // Log the message using the default logger
      // ...
    }
  }
```