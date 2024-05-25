```java
  import org.cactoos.text.UncheckedText;

  public class RtTransaction {

    public String getTransactionId(String transactionId) {
      return new UncheckedText(transactionId).asString();
    }

  }
```