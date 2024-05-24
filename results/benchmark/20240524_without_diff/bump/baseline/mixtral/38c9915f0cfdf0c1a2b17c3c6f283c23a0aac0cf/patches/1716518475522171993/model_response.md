Here's a possible patch for the client code:
```java
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String hash) {
  this.hash = new UncheckedText(hash);
  // ...
}
```
This patch replaces the usage of `SplitText` with `UncheckedText`, which is a new class added in the updated library version. This class can be used in a similar way as `SplitText`, but it doesn't validate the input string for null or empty values. In this case, we use it to wrap the `hash` parameter of the `RtTransaction` constructor.