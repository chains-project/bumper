Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  try (Input in = new UrlInput(url(id))) {
    return new LengthOf(in).longValue();
  }
}
```
Explanation:
- I changed the import statement to use `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`.
- I updated the code inside the `score` method to create a new `LengthOf` object using the `Input` object, and then called the `longValue` method to get the length.
- I assumed that the `UrlInput` class is available and properly implemented.
- I also assumed that the `url` method is defined and returns a `String` representing the URL for the given ID.