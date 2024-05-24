Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  double result = 0;
  try (Input input = new UrlInput(baseUrl + id)) {
    result = new LengthOf(input).intValue();
  }
  return result;
}
```
In this patch, I replaced the `org.cactoos.iterable.LengthOf` import with `org.cactoos.scalar.LengthOf` and updated the code accordingly. The `UrlInput` is assumed to be available in the client code.