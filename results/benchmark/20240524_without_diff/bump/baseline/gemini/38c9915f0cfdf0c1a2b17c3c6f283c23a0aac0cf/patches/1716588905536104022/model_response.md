```java
  import org.cactoos.text.FormattedText;
  import org.cactoos.text.TextOf;

  public class RtTransaction {

    public String getTransactionId() {
      return new FormattedText("Transaction ID: %s", new TextOf(this.transactionId)).asString();
    }

    private final String transactionId;

    public RtTransaction(String transactionId) {
      this.transactionId = transactionId;
    }
  }
```