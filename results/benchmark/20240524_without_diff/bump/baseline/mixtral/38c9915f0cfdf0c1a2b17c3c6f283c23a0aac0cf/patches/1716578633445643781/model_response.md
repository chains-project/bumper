Here's the proposed patch for the failing client code:

```java
import org.cactoos.Iterable;
import org.cactoos.iterable.Iterables;

// ...

public double rtScore(String userId) throws IOException {
  long start = System.currentTimeMillis();
  Iterable<Transaction> txs = api.transactionsOf(userId);
  long end = System.currentTimeMillis();
  return Iterables.size(txs) / (end - start) * 1000.0;
}
```

In this patch, I replaced the usage of `LengthOf` class with the `Iterables.size()` method, which is available in the `cactoos` library and serves the same purpose. By doing this, we avoid the need for an external dependency update.