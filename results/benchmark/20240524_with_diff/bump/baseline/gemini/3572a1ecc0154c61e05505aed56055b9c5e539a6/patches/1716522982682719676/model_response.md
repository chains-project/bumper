```java
import org.apache.thrift.TConfiguration;
import org.apache.thrift.transport.*;

public class AppenderUtils {

    public static TTransport createTransport(String host, int port) {
        TConfiguration configuration = new TConfiguration();
        configuration.setSocketTimeout(30000);
        return new TFramedTransport(new TSocket(host, port, configuration));
    }
}
```