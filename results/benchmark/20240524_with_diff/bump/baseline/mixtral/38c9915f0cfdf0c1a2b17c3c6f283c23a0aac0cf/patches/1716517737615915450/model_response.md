Here's a possible patch for the failing client code:

```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  try (Input input = new UrlInput(url(id))) {
    return new LengthOf(input).longValue();
  }
}
```

In this patch, we've imported the new `LengthOf` class from the `org.cactoos.scalar` package, and used it to compute the length of the input `URL`. Note that the `UrlInput` class from the previous version has not been removed, so it can still be used to create an `Input` instance from a `URL`.