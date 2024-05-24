Here's the fixed version of the code that replaces the failing import:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.Trimmed;

// ...

new Trimmed(new TextOf(new IoCheckedText(input)));
```

In this version, we use the `TextOf` class to convert the `IoCheckedText` to a `Text` object, and then apply the `Trimmed` decorator to remove any leading or trailing whitespace from the text.