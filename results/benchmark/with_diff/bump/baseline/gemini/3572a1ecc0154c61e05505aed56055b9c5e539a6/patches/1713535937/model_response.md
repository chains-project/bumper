```java
import org.apache.thrift.TConfiguration;
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.InputStream;
import java.io.OutputStream;

public class AppenderUtils {

    public static TIOStreamTransport createThriftTransport(InputStream inputStream, OutputStream outputStream) {
        return new TIOStreamTransport(new TConfiguration(), inputStream, outputStream);
    }
}
```