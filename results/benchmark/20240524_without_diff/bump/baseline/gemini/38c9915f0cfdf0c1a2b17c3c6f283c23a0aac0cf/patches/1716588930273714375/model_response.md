```java
import org.cactoos.text.FormattedText;

public class RtTransaction {

    public String getTransactionStatus(String transactionId) {
        return new FormattedText(
                "SELECT status FROM transactions WHERE id = %s",
                transactionId
        ).asString();
    }
}
```