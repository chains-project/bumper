Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  try (Input input = api().input(id)) {
    return new LengthOf(input).longValue();
  }
}
```
In this patch, we've imported the newly added `LengthOf` class from the `org.cactoos.scalar` package, and used it to calculate the length of the input. Note that the `longValue()` method is used to convert the scalar value to a `long`, which can then be returned as a `double`.