Here's the proposed patch:

```java
import org.cactoos.text.TextOf;

// ...

public RtTransaction(String data) {
  this.data = new TextOf(data).asString();
}
```

This patch replaces the usage of `TrimmedText` with a new method `TextOf`, which converts a `String` to a `Text` object. The `TextOf` method is an added method in the new library version. The `asString()` method is then called on the `TextOf` object to get the string value.