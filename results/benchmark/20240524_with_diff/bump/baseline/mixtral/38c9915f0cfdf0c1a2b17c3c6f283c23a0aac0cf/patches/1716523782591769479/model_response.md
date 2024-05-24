Here is a patch that you can apply to the client code to fix the error:

```java
import org.cactoos.bytes.BytesOf;
import org.cactoos.text.TextOf;

// ...

@Override
public Text text() {
  return new TextOf(BytesOf.bytes(password.getBytes()));
}
```

This patch replaces the use of the removed `Text$NoNulls` class with the new `TextOf` class, which can be used to create a `Text` instance from a `byte[]`. The `BytesOf` class is used to convert the password string to a `byte[]`.

Note that this patch assumes that the `password` field is a `String`. If `password` is not a `String`, you will need to modify the code accordingly.