Sure, here's a possible patch for the failing code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double rtScore(String url) throws IOException {
  try (InputStream in = new URL(url).openStream()) {
    return new LengthOf(in).intValue();
  }
}
```
Here, I changed the import statement to use `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`. I also changed the return type of the `LengthOf` object from `int` to `double`, since the method signature specifies a return type of `double`. Finally, I updated the code to use the `LengthOf` constructor that takes an `InputStream` as its argument.