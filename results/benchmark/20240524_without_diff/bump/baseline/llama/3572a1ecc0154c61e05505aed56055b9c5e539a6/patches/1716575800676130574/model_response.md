```java
import org.apache.thrift.transport.TTransport;

// ...

public class AppenderUtils {
    // ...
    public void configureLogger() {
        TTransport transport = new TTransport();
        // ...
    }
    // ...
}
```