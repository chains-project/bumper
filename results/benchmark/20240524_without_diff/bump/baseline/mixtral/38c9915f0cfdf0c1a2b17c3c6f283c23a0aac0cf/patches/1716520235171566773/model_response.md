Here's the fixed version of the failing code:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String id, TextEnvelope<String> envelope) {
  super(id, new UncheckedText(new Trimmed(envelope.asString())));
}
```

The change is using `UncheckedText` and `Trimmed` to wrap the `envelope.asString()` instead of directly using `TrimmedText`. This way, the code uses only the added library methods and avoids the removed `TrimmedText` class.