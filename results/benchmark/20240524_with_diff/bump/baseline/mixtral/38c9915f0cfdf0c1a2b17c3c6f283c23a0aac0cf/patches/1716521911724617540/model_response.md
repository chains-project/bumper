Here's the proposed patch for the failing client code:

```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(String hash, InputStream input, RtDb db) throws IOException {
  super(hash);
  this.input = Objects.requireNonNull(input);
  this.db = Objects.requireNonNull(db);
  this.len = new LengthOf(input); // replace LengthOf(new IterableInputStream(input)) with new LengthOf(input)
}
```

In the updated library version, the `LengthOf` class has been moved from `org.cactoos.iterable` to `org.cactoos.scalar`. The constructor signature has also changed, and now accepts an `Iterable` or `Input` instead of an `IterableInputStream`. In the client code, replace `LengthOf(new IterableInputStream(input))` with `new LengthOf(input)` to fix the error.