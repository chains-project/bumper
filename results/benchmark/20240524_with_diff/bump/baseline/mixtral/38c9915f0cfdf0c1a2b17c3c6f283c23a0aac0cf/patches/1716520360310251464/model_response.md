Here's the proposed patch:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(RtTransactionContext context, RtTransactionParent parent, TextEnvelope title) {
    super(context, parent, new UncheckedText(new TrimmedText(title).asString()));
    // ...
}
```

This patch wraps the `title` TextEnvelope with an UncheckedText and a TrimmedText. This ensures that the TrimmedText is compatible with the new library version while still maintaining the same behavior as before.