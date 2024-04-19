```java
import org.apache.thrift.transport.TIOStreamTransport;

public class AppenderUtils {

    /**
     * Creates a TFastFramedTransport from the given input stream.
     *
     * @param inputStream The input stream to use.
     * @return A new TFastFramedTransport instance.
     */
    public static TIOStreamTransport createTFastFramedTransport(java.io.InputStream inputStream) {
        return new TIOStreamTransport(null, inputStream);
    }
}
```