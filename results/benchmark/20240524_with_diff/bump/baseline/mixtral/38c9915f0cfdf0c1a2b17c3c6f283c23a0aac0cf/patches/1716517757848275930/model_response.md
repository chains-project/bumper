Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  double sum = 0.0;
  try (Input input = new Utf8(new Html(new Api().page(id)))) {
    for (String line : new Lines(input)) {
      sum += new LengthOf(new Text(line)).intValue();
    }
  }
  return sum;
}
```
In this patch, I replaced the `LengthOf` import from `org.cactoos.iterable` to `org.cactoos.scalar`, since the `LengthOf` method for `Text` has been moved there. Additionally, I updated the usage of `LengthOf` with the new import, and explicitly converted the result to an `int` using the `intValue()` method.