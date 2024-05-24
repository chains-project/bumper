Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(TransactionDao dao, Iterable<Transaction> txs) {
  this.dao = Objects.requireNonNull(dao);
  this.txs = Objects.requireNonNull(txs);
  this.len = new LengthOf<Transaction>(txs);
}
```
The only change made is to replace `org.cactoos.iterable.LengthOf` with `org.cactoos.scalar.LengthOf`. This is possible because the new version of the library includes a constructor for `LengthOf` that takes an `Iterable` as an argument.