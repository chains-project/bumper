Here's a fixed version of the failing method in `SimpleThriftLogger.java`:

```java
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;

private TTransport createTransport(String host, int port) {
  return new TSocket(host, port);
}
```

This version of the method uses `TSocket` instead of `TFramedTransport`. The `TSocket` class is part of the Thrift library, and it is still available and functional, so it should work as a replacement for the failing code. However, note that this change may result in a slightly different behavior, since `TFramedTransport` provides additional framing functionality compared to `TSocket`. Make sure to test the updated code thoroughly.