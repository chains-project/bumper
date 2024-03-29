Here is a potential fix for the issue:
```java
import org.cactoos.text.TextCollector;
import org.cactoos.text.Joined;

// ...

@Override
public TextWallets wallets(TextCursor cursor) throws IOException {
  return new Joined(
    "; ",
    new TextCollector(
      cursor.stream()
        .map(CursorIn::new)
        .toArray(CursorIn[]::new)
    )
  );
}
```
This fix uses the `TextCollector` and `Joined` classes from the `org.cactoos.text` package to concatenate the text from the `TextCursor` into a single string. The `TextCollector` is used to convert the `TextCursor` into a stream of `CursorIn` objects, which can then be joined together using the `Joined` class. This should resolve the issue with the missing `JoinedText` class.