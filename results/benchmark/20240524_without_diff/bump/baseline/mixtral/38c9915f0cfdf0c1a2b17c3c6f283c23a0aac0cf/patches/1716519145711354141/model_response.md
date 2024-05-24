Here's the fixed version of the client code:

```java
import org.cactoos.text.Joined;

// ...

public class WalletsIn {
    // ...

    @Override
    protected Text asText() {
        return new Joined(" ", new Text[] {
            new BytesOf(new TextOf("Name")),
            new BytesOf(new TextOf("Balance")),
            new BytesOf(new TextOf("Status"))
        });
    }
}
```

In this updated version, I replaced the `JoinedText` class with the new `Joined` class, which serves the same purpose. I also replaced the `TextOf` constructor that accepts a `String` and a `Charset` with the new `TextOf` constructor that accepts a `String` only, and added a `BytesOf` wrapper around it. This way, the code uses only the added methods from the new library version.