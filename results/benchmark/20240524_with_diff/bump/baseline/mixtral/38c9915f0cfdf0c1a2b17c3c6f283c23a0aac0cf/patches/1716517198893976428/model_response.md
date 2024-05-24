Here's a patch that you can apply to fix the error:
```java
import org.cactoos.io.Joined;

//...

JoinedText joined = new JoinedText(", ", new Joined<>(
    input -> new TextOf(input),
    iterable
));
```
This code creates a new `Joined` object using the new `Joined` constructor that takes an iterator function and an iterable. The iterator function creates a new `TextOf` object for each input element. The resulting `Joined` object can then be used to join the elements together with a comma and a space between each element.