```java
import org.cactoos.text.TrimmedText;

public class RtTransaction {

    public String getTransactionId() {
        String transactionId = null;
        try {
            transactionId = new TrimmedText(this.getRequest().getTransactionId()).asString();
        } catch (Exception e) {
            // Handle exception
        }
        return transactionId;
    }
}
```