```java
import org.cactoos.text.TextOf;
import java.io.IOException;

public class RtTransaction {

    /**
     * --
     */
    public static String getTransactionId(String url) throws IOException {
        return new TextOf(url).split("/").last();
    }
}
```