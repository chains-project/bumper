Here is a patch that you can apply to the client code to fix the error:

```java
import org.cactoos.text.TextOf;

// ...

Text randomText = new TextOf("some random text");
```

This patch replaces the usage of `RandomText` with a new class `TextOf` which is used to create a new `Text` instance from a given `CharSequence`. The `TextOf` class is a new addition in the updated library version.

Note that this patch assumes that the client code only needs a simple text instance with a fixed value. If the original code required a truly random text, you may need to modify the argument passed to `TextOf` constructor to generate a random text in a different way.