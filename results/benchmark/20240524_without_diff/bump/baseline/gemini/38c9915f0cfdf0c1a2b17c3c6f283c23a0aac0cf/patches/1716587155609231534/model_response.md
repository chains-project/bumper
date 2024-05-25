```java
import org.cactoos.text.TrimmedText;

public class RtTransaction {
    public String getTransactionId() {
        String transactionId = "1234567890";
        return new TrimmedText(transactionId).asString();
    }
}
```