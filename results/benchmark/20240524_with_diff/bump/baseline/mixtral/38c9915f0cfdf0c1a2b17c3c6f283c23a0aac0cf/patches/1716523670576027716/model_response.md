Here's the patched code:

```java
import org.cactoos.text.TextOf;
import java.time.LocalDateTime;

// ...

Text randomText = new TextOf(LocalDateTime::now);
```

This code replaces the failing import and the instantiation of the `RandomText` class with a new instantiation of the `TextOf` class, which is an added method in the new library version. The `TextOf` class can take a `Scalar` as a parameter, and we're using a method reference (`LocalDateTime::now`) to create a `Scalar` that returns the current date and time. This should fix the "cannot find symbol" error.