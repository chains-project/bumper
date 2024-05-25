```java
  import org.cactoos.text.UncheckedText;

  public class RtTransaction {
    public static String getTransactionId(String transactionId) {
      return new UncheckedText(transactionId).asString();
    }
  }
```