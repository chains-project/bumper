```java
import org.apache.thrift.transport.TTransport;

import com.pinterest.singer.thrift.transport.TFramedTransport;

public class SimpleThriftLogger {

    public static TTransport getFramedTransport(TTransport underlyingTransport) {
        return new TFramedTransport(underlyingTransport);
    }
}
```