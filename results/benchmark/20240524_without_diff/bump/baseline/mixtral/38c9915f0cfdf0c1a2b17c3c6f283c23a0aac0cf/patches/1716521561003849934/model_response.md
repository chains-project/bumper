Here's the proposed patch:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.TextOfScalar;

// ...

public RtTransaction(Transaction transaction,
    @Named("amount") Scalar<BigDecimal> amount,
    @Named("currency") Scalar<String> currency,
    @Named("timestamp") Scalar<Instant> timestamp) {
  this.transaction = Objects.requireNonNull(transaction);
  this.amount = Objects.requireNonNull(new TextOfScalar<BigDecimal>(amount));
  this.currency = Objects.requireNonNull(new TextOfScalar<String>(currency));
  this.timestamp = Objects.requireNonNull(new TextOfScalar<Instant>(timestamp));
}
```

In this patch, I replaced the usage of `TrimmedText` with `TextOfScalar`, which is a new class in the updated library. This class converts a `Scalar` to a `Text`, which can be used in the same way as `TrimmedText`. I also added imports for the new classes.