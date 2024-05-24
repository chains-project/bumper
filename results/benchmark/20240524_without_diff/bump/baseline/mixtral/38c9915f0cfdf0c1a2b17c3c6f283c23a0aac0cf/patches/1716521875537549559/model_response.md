Here's the proposed patch for the failing client code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtWallet from, RtWallet to, RtAmount amount, RtCode code) {
  this.from = from;
  this.to = to;
  this.amount = amount;
  this.code = code;
  this.id = new LengthOf<>(Iterables.iterate(txs, tx -> tx.id())).intValue();
}
```
In this patch, I replaced the old `LengthOf` import with the new one from the `org.cactoos.scalar` package, which is an added method in the new library version. The rest of the code remains unchanged.