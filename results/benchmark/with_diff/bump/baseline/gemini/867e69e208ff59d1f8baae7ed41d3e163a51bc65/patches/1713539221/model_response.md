```java
import org.apache.thrift.transport.TTransport;

  public void log(String message) {
    TTransport transport = new TTransport();
    transport.write(message.getBytes());
    transport.flush();
  }
```