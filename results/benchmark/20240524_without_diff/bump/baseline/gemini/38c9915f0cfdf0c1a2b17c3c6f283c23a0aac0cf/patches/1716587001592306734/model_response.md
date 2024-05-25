```java
import org.cactoos.text.TrimmedText;

public class RtTransaction {

    public String getTransactionId() {
        return new TrimmedText(this.transactionId).asString();
    }

}
```