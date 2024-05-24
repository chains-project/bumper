Here is the proposed patch:

```java
import org.cactoos.io.Joined;

// ...

public class WalletsIn {
    // ...

    private String join(Iterable<String> parts) {
        return new Joined(
            String::valueOf,
            parts
        ).asString();
    }

    // ...
}
```

This patch replaces the usage of `JoinedText` with `Joined` from the `org.cactoos.io` package, which is an addition in the new library version. The `join` method takes an `Iterable` of `String`s and joins them using the `String.valueOf` function. This method can be used to replace the usage of `JoinedText` in the original code.