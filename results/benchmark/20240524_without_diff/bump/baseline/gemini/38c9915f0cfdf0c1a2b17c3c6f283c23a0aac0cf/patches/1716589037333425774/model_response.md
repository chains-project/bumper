```java
import org.cactoos.text.FormattedText;

public class RtTransaction {

    public String getTransactionId() {
        return new FormattedText("%s - %s", "Transaction", "123456").asString();
    }
}
```