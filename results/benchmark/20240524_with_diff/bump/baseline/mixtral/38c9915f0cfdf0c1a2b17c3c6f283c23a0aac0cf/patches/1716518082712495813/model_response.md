Here is the proposed patch:

```java
import org.cactoos.text.TextOf;

// ...

public RtTransaction(String raw) {
  this.raw = new TextOf(raw).asString();
  // ...
}
```

This patch replaces the usage of `TrimmedText` with `TextOf`, which is a new class added in the updated library version. The `TextOf` class can convert a `CharSequence` to a `String` using its `asString()` method. This allows us to achieve the same functionality as the original code while avoiding the use of the removed `TrimmedText` class.