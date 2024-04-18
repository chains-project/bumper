Here's the proposed patch for the failing method in `AppenderUtils.java`. This patch replaces the failing import statement and uses the `TFramedTransport` instead of the deprecated `TFastFramedTransport`.

```java
import org.apache.thrift.transport.TFramedTransport;

// ...

public static TTransport newFramedTransport(TTransport transport) {
  if (transport instanceof TFramedTransport) {
    return (TFramedTransport) transport;
  }
  return new TFramedTransport(transport);
}
```

This patch assumes that the `TFramedTransport` class is available in the project's classpath, and the issue is caused by the deprecation of the `TFastFramedTransport` class.