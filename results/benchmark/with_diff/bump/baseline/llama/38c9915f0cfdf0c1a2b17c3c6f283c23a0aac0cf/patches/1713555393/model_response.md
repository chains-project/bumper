Here's a proposed patch to fix the error:
```java
import org.cactoos.text.Text;

public class WalletsIn {
    private final JoinedText joinedText = new JoinedText(Text.of("Wallets"), Text.of("In"));
}
```
The `JoinedText` class has been removed in the new version of the library, so we're replacing it with the `Text` class and creating a `JoinedText` object using the `Text.of()` method. This should fix the error and allow the code to compile.