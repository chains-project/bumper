```java
  import org.cactoos.scalar.UncheckedScalar;
  import org.cactoos.scalar.Unchecked;

  import java.util.function.Function;

  public class RtTransaction {

    private final Function<UncheckedScalar<String>, UncheckedScalar<String>> transaction;

    public RtTransaction(Function<UncheckedScalar<String>, UncheckedScalar<String>> transaction) {
      this.transaction = transaction;
    }

    public UncheckedScalar<String> execute(UncheckedScalar<String> request) {
      return transaction.apply(request);
    }

  }
```