Here's the fixed version of the code that uses the new `Joined` class from `org.cactoos.io` package:

```java
import org.cactoos.io.Joined;
import org.cactoos.Text;

public class WalletsIn {
    // ...

    private Text joined(Iterable<Text> parts) {
        return new Joined(
            " ",
            IterableOf.<Text>of(
                new TextOf("balance: "),
                new FormattedText("%.2f", parts),
                new TextOf("\n")
            )
        );
    }

    // ...
}
```

In this version, we use the new `Joined` class from `org.cactoos.io` package, which is an iterable version of the `JoinedText` class from the previous version. We also use the `FormattedText` class from `org.cactoos.text` package to format the balance value as a floating-point number with two decimal places.

Note that we changed the method signature to take an `Iterable<Text>` instead of a single `Text` object. This allows us to pass multiple text objects to the method and join them using the `Joined` class. We also changed the `TextOf` constructor to take an `Iterable` of `Text` objects instead of a single `String` object.

Finally, we created a new `IterableOf.<Text>of` method to create an `Iterable` of `Text` objects from the `parts` argument. This method is not part of the Cactoos library, but it can be easily implemented as follows:

```java
public class IterableOf<T> implements Iterable<T> {
    private final Iterable<T> source;

    public IterableOf(Iterable<T> source) {
        this.source = source;
    }

    @Override
    public Iterator<T> iterator() {
        return source.iterator();
    }

    public static <T> IterableOf<T> of(Iterable<T> source) {
        return new IterableOf<>(source);
    }
}
```

This class simply wraps an existing `Iterable` object and delegates the `iterator()` method to it. It also provides a convenient `of` method to create an instance of the class.