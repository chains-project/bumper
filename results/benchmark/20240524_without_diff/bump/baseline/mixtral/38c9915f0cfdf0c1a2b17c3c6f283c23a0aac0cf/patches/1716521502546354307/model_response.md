Here's a fixed version of the code that replaces the failing import statement and uses the added `UncheckedBytes` class instead of the removed `UncheckedScalar` class:

```java
import org.cactoos.bytes.UncheckedBytes;

// ...

public RtTransaction(DbApi db, Scalar<Transaction> tx, Scalar<Block> blk) {
  this.db = db;
  this.tx = tx;
  this.blk = blk;
  this.bytes = new UncheckedBytes(
    new BytesOf(() -> tx.value().payload().getBytes(StandardCharsets.UTF_8))
  );
}
```

This code creates a new `UncheckedBytes` object that wraps a `BytesOf` object, which in turn wraps a lambda expression that converts the transaction payload to a byte array using `StandardCharsets.UTF_8`. This should achieve the same functionality as the original code while using only the new library methods.