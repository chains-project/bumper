It seems there's an issue with an incorrect import statement. The `JoinedText` class from the `org.cactoos.text` package might have been removed or renamed in the newer version of the library.

Considering the error message and the assumption that you can only work on the client code, you can replace the failing import statement with the following code:

```java
import java.util.stream.Collectors;

// ...

new JoinedText("", Arrays.stream(messages).collect(Collectors.toList()).toArray(new String[0]));
```

This code snippet replaces the problematic import and uses the Java 8 `Streams` API to join the messages. Since the `JoinedText` class is not available in the recent version, this patch should resolve the issue.

Note that you may need to replace `messages` with the actual variable used in the original code, as I don't have the complete method implementation.

Additionally, you might need to adjust the constructor arguments for the `JoinedText` class, if the original constructor arguments were different from an empty string and the messages list.