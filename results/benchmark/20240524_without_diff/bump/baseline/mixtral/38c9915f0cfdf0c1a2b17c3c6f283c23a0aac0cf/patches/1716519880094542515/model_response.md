Here's the proposed patch for the failing client code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(Exchange exchange) throws IOException {
  double sum = 0.0;
  try (Input input = inputOf(exchange)) {
    for (String line : LinesOf.lines(input)) {
      sum += new LengthOf<>(line).intValue();
    }
  }
  return sum;
}
```
In this patch, I replaced the `LengthOf` import from `org.cactoos.iterable` to `org.cactoos.scalar`, as the `LengthOf` class has been moved there. Also, I changed the way we get the length of a string from using `LongOf` to `LengthOf`, as the former has been removed in the new version.