Here's a possible patch to fix the error:
```java
import org.cactoos.io.Joined;

//...

JoinedText joinedText = new JoinedText(", ", new Joined<>(
    input -> new UncheckedText(input),
    iterable
));
```
This code creates a `Joined` object that takes an iterable of `UncheckedText` objects, where each `UncheckedText` object is created from an input string using the `UncheckedText` constructor. The `Joined` object is then converted to a `JoinedText` object using the `JoinedText` constructor that takes a separator and an iterable of `Text` objects. The `Text` objects are created from the inputs using the `UncheckedText` constructor.

Note that the `JoinedText` class has been removed in the new version of the library, so we use the `Joined` class instead. We also use the `UncheckedText` class to convert the input strings to `Text` objects, since the `TextOf` class has been removed.