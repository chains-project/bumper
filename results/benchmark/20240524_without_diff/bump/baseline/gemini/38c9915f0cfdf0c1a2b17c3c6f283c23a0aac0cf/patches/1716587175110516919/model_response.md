```java
  import org.cactoos.text.TrimmedText;

  import java.util.function.Supplier;

  public class RtTransaction {

    private final Supplier<String> transactionIdSupplier;

    public RtTransaction(Supplier<String> transactionIdSupplier) {
      this.transactionIdSupplier = transactionIdSupplier;
    }

    public String getTransactionId() {
      return new TrimmedText(transactionIdSupplier.get()).asString();
    }
  }
```