```java
  import org.cactoos.text.TrimmedText;

  public class RtTransaction {

    public static String getTransactionId(String transactionId) {
      return new TrimmedText(transactionId).asString();
    }
  }
```