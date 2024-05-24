Here's the proposed patch for the failing client code:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.UncheckedText;

// ...

@Override
public Transaction create(String raw) throws IOException {
    TextEnvelope envelope = new TextEnvelope(
        new UncheckedText(raw)
    );
    // ... continue with the rest of the method
}
```

This patch replaces the `TrimmedText` import with `TextEnvelope` and `UncheckedText` imports, and wraps the raw input in a `TextEnvelope` instead of using `TrimmedText`. This should resolve the compilation error.