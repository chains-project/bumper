```java
import org.apache.thrift.TConfiguration;
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.IOException;

public class AppenderUtils {
  public static TIOStreamTransport createTIOStreamTransport(TConfiguration config) throws IOException {
    return new TIOStreamTransport(config, System.out);
  }
}
```