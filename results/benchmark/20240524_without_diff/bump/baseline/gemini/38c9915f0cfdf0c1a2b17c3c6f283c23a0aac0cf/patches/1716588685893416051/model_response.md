```java
import org.cactoos.time.ZonedDateTimeOf;

public class RtTransaction {
  public static String getTransactionId(String transactionId) {
    return new ZonedDateTimeOf(transactionId).toString();
  }
}
```