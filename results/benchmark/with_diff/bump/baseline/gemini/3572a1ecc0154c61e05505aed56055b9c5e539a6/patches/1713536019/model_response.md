```java
import org.apache.thrift.TConfiguration;
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.transport.TTransport;

import java.io.InputStream;
import java.io.OutputStream;

public class AppenderUtils {

    public static TTransport createTransport(InputStream inputStream, OutputStream outputStream, TConfiguration configuration) {
        return new TIOStreamTransport(configuration, inputStream, outputStream);
    }
}
```