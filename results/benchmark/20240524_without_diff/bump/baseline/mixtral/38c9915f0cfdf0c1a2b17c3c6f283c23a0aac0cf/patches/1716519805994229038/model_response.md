Here's a possible patch for the failing client code:

```java
import org.cactoos.scalar.LengthOf;

// ...

public double rtScore(String url) throws IOException {
    // ...
    long len = new LengthOf<Iterable<Byte>>(
        Iterables.forBasedIterator(
            new InputStreamToIterator(
                new UrlToInputStream(url)
            )
        )
    ).intValue();
    // ...
}
```

This patch imports the new `LengthOf` class from `org.cactoos.scalar` and uses it to compute the length of the input stream. It does this by creating an iterator from the input stream, wrapping it in an `Iterable`, and then passing it to the `LengthOf` constructor. The `intValue()` method is called on the `LengthOf` object to get the length as an `int`. This value can then be used in the rest of the method.