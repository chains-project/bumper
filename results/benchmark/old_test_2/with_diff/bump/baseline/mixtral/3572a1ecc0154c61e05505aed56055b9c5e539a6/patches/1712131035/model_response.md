Here's the proposed patch:

```java
import org.apache.thrift.transport.TIOStreamTransport;

// ...

public class AppenderUtils {
  // ...

  @Override
  public TFramedTransport getFramedTransport() {
    TConfiguration configuration = new TConfiguration();
    return new TFramedTransport(new TIOStreamTransport(configuration));
  }

  // ...
}
```

This patch replaces the usage of `TFastFramedTransport` with `TIOStreamTransport`, which is a new addition in the library. The `TIOStreamTransport` can be used to wrap an existing `TConfiguration`, and it can be used to create a `TFramedTransport`.