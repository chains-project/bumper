Here is the proposed patch:
```java
import org.cactoos.text.TextEnvelope;

// ...

public RtTransaction(String hash, TextEnvelope title, TextEnvelope amount, TextEnvelope fee, TextEnvelope timestamp) {
  // ...
}
```
The `TrimmedText` class has been removed in the new version, so we need to replace it with an alternative. In this case, I have used the `TextEnvelope` class, which allows us to apply any text transformer to the text. This way, we can still trim the text if needed.

Note that you will need to update the code that creates the `title`, `amount`, `fee`, and `timestamp` parameters to use `TextEnvelope.envelope(text)` instead of `new TrimmedText(text)`. For example:
```java
TextEnvelope title = TextEnvelope.envelope(new Joined(", ", new TextOf("Mr.", name, " ", lastName), new TextOf(" (", email, ")")));
```
This will ensure that the text is properly trimmed before being passed to the `RtTransaction` constructor.