Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  try (Input input = new Api().input(id)) {
    return new LengthOf(input).longValue();
  }
}
```
In this patch, we have imported the new `LengthOf` class from the `org.cactoos.scalar` package and used it to calculate the length of the input. The `longValue()` method is called to convert the result to a `double` as required by the original method signature.