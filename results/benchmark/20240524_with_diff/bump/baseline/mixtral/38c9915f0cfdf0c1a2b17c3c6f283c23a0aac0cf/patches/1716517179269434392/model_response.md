Here's a possible patch that you can apply to the failing client code:

```java
import org.cactoos.text.Joined;
import org.cactoos.text.Text;

...

Text joined = new Joined(
  "Failed to create wallet: ",
  new TextOf(ex.getMessage())
);
```

This patch replaces the `JoinedText` class with the `Joined` class, which provides similar functionality and is available in the updated library version. The `TextOf` class is used to convert the exception message to a `Text` object, which can be used with the `Joined` class.