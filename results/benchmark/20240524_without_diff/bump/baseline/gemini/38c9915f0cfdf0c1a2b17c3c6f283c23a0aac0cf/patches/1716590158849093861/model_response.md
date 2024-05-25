```java
import org.cactoos.text.SplitText;
import java.util.Arrays;

public class RtTransaction {

    public static String[] splitTransaction(String transaction) {
        return new SplitText(transaction, "\n").asList().stream().flatMap(Arrays::stream).toArray(String[]::new);
    }
}
```