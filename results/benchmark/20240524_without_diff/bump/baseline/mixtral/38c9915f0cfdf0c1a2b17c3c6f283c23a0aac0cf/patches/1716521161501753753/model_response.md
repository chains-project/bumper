Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  try (Input in = new UrlInput(new URL(api + "/accounts/" + id))) {
    return new LengthOf(in).longValue();
  }
}
```
In this patch, I replaced the import statement to use the new `LengthOf` class from the `org.cactoos.scalar` package. Additionally, I changed the return type of the `LengthOf` instance to `long` using the `longValue()` method.