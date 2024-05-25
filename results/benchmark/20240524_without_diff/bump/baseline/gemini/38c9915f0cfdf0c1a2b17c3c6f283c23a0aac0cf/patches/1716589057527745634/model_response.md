```java
import org.cactoos.text.TrimmedText;

public class RtTransaction {

    public String getTransactionHash() {
        return new TrimmedText(this.getRawTransactionHash()).asString();
    }

    private String getRawTransactionHash() {
        return this.transactionHash;
    }

    private final String transactionHash;

    public RtTransaction(String transactionHash) {
        this.transactionHash = transactionHash;
    }
}
```