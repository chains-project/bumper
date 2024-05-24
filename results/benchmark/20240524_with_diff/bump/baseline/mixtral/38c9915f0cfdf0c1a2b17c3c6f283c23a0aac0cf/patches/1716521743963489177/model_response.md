Here is a possible patch for the client code:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

// ...

public class RtTransaction {
  // ...
  @Override
  protected String value() {
    return new TextOf(
      new UncheckedText(
        new TextOf(
          new TextOf(
            new TextOf(new Trimmed(new TextOf(super.value())))
          )
          .asString()
        )
        .asBytes()
      )
      .asString()
    ).asString();
  }
  // ...
}
```

This patch uses the `TextOf` and `UncheckedText` classes from the new library version to convert the result of the `super.value()` method to a `Text` object, then trims the whitespace from the text, converts it to bytes, and converts it back to a string. This should produce the same result as the original code, but using only the methods that are present in the new library version.