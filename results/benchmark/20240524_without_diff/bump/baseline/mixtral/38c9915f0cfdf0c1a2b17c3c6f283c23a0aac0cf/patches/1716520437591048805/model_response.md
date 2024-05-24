Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction of(RtTransactionId id, RtTransactionData data) {
    Iterable<RtTransactionEntry> entries = data.entries();
    int size = new LengthOf<RtTransactionEntry>(entries).intValue();
    // ...
}
```
In this patch, I replaced the `LengthOf` import from `org.cactoos.iterable` to `org.cactoos.scalar` since the `LengthOf` class has been moved there. The rest of the code remains the same.