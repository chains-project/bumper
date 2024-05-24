Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

...

public Double rtScore(String user) throws IOException {
    ...
    long itemsLength = new LengthOf<Iterable<Transaction>>(txs).value();
    ...
}
```
In this patch, we've imported the new `LengthOf` class from the `org.cactoos.scalar` package, and used it to calculate the length of the `txs` iterable. This should resolve the "cannot find symbol" error caused by the updated library.