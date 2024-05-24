Sure, I can help with that. Here's a modified version of your code that should work with the updated library:
```java
import org.cactoos.text.BytesOf;
import org.cactoos.text.TextOf;

// ...

public class Wallet {
    // ...

    private TextOf name;

    @Override
    public void init(final Map<String, String> params) throws IOException {
        this.name = new TextOf(
            new BytesOf(
                new Split(
                    ":",
                    new TextOf(params.get("name"))
                )
            )
            .asBytes()
        );
        // ...
    }

    // ...
}
```
In this modified version, I replaced the `SplitText` class with the `Split` class from the updated library. I also added a `BytesOf` class to convert the resulting `Iterable<Byte>` to a `Text` object. Finally, I added a `TextOf` class to convert the `Text` object to a `String`. This should allow you to split the `name` parameter by the colon character and get the first part of the resulting array as a `String`.