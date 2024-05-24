Here's a patch that you can apply to the client code in order to fix the error:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.Trimmed;

// ...

new Trimmed(new TextOf(new String(originalBytes)));
```

This code creates a `TextOf` object that converts a `byte[]` array to a `String`, and then applies a `Trimmed` filter to remove any leading or trailing whitespace. You can replace the `originalBytes` variable with the actual `byte[]` array that you are working with.