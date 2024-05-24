Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  try (Input in = api().input(id)) {
    return new LengthOf(in).intValue();
  }
}
```
In this patch, I replaced the import statement to use the new `LengthOf` class in the `org.cactoos.scalar` package. Additionally, I changed the return type of the `LengthOf` instance to `int` using the `intValue()` method.