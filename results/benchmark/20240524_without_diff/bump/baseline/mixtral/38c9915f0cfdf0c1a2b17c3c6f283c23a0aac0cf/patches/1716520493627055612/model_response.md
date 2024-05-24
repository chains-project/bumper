Here's the proposed patch to fix the error:

```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtTransactions transactions, RtTransactionId id,
    RtTransactionState state, RtTransactionLog log, RtTransactionData data) {
    super(transactions, id, state, log, data);
    this.amount = new LengthOf<>(data.asIterable());
}
```

In this patch, I replaced the old `LengthOf` import with the new one from the `org.cactoos.scalar` package. The `LengthOf` constructor has also been changed accordingly to take an `Iterable` instead of directly taking the `RtTransactionData`.