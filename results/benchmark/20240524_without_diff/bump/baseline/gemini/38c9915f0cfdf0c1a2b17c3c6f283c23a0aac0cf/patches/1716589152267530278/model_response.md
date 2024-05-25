```java
  import org.cactoos.text.TrimmedText;

  import java.util.Optional;

  public class RtTransaction {

    private final String transactionId;

    public RtTransaction(final String transactionId) {
      this.transactionId = new TrimmedText(transactionId).asString();
    }

    public Optional<String> getTransactionId() {
      return Optional.ofNullable(this.transactionId);
    }
  }
```