Here's the proposed patch:

```java
import org.apache.thrift.transport.TFramedTransport;

// ...

@Override
public TTransport createTransport() {
  try {
    return new TFramedTransport(socket);
  } catch (TTransportException e) {
    throw new RuntimeException("Failed to create framed transport", e);
  }
}
```

In this patch, I replaced `TFastFramedTransport` with `TFramedTransport` from the same package. The `TFastFramedTransport` class was removed in a newer version, so using `TFramedTransport` is a suitable alternative.