Here is a possible patch for the client code:

```java
import org.cactoos.text.BytesOf;
import org.cactoos.text.UncheckedText;

...

public class RtTransaction {
  ...
  @Override
  public Transaction fromBytes(byte[] bytes) throws IOException {
    Text of = new BytesOf(new UncheckedText(new String(bytes, UTF_8)));
    ...
  }
  ...
}
```

This patch replaces the use of `SplitText` with `BytesOf` and `UncheckedText` to convert the byte array to a `Text` object. The `UncheckedText` class is used to wrap the string obtained from the byte array, since it is a new class that was added in the updated library version.