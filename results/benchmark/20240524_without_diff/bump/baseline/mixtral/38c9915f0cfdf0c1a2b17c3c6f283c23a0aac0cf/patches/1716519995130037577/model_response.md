Sure, here's a possible patch for the failing code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double rtScore(String... args) throws IOException {
  Iterable<Double> doubles = // your code to get an iterable of doubles
  return new LengthOf(doubles).longValue();
}
```
In this patch, we've imported the new `LengthOf` class from the `org.cactoos.scalar` package instead of the old one from `org.cactoos.iterable`. We then use this new `LengthOf` class to get the length of the `Iterable` of doubles, which is returned as a `long` value. Note that the `longValue()` method is used to convert the `Scalar` returned by `LengthOf` to a `long` value.