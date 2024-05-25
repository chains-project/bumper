```java
  import org.cactoos.text.TrimmedText;
import com.google.common.base.Preconditions;

public class RtTransaction {

  public static final String TRANSACTION_ID_PATTERN = "^[0-9a-f]{64}$";
  public static final String TRANSACTION_ID_PATTERN_ERROR_MESSAGE = "Transaction ID must be a 64-character hexadecimal string";
  public static final String TRANSACTION_ID_PATTERN_ERROR_CODE = "transaction_id_pattern_error";

  private final String transactionId;

  public RtTransaction(String transactionId) {
    Preconditions.checkArgument(transactionId.matches(TRANSACTION_ID_PATTERN), TRANSACTION_ID_PATTERN_ERROR_MESSAGE, TRANSACTION_ID_PATTERN_ERROR_CODE);
    this.transactionId = transactionId;
  }

  public String getTransactionId() {
    return transactionId;
  }

  public String getTransactionIdWithPrefix(String prefix) {
    return new TrimmedText(prefix + transactionId).asString();
  }
}
```