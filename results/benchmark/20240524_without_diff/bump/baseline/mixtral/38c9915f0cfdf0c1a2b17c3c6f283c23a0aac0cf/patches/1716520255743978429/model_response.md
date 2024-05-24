Here's a possible patch for the client code:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

// ...

public class RtTransaction {
  // ...
  @Override
  public Transaction fromJson(final String json) {
    final UncheckedText jsonText = new UncheckedText(json);
    // ...
    final TextOf<CharSequence> trimmedText = new TextOf<>(
      new Trimmed(jsonText)
    );
    // ...
  }
  // ...
}
```

This patch replaces the usage of `TrimmedText` with `Trimmed` and `TextOf`. The `Trimmed` class is still available in the new library version, and it can be used in combination with `TextOf` to achieve the same functionality as the original `TrimmedText`.