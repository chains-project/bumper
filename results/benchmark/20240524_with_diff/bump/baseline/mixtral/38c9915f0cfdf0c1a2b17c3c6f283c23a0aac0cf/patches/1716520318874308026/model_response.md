Here's the fixed version of the failing client code:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.Trimmed;

// ...

public RtTransaction(String raw) {
  this.raw = new Trimmed(new TextOf(raw));
  // ...
}
```

The change is to replace the import statement for `TrimmedText` with `Trimmed` and `TextOf`, and then wrap the `raw` argument in a `TextOf` and `Trimmed` to create the `this.raw` field. This uses the added library method `TextOf` and `Trimmed` to achieve the same functionality as the original code.