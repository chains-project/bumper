Here's a possible patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Sticky of;

// ...

@Override
public double score(CurrencyId id) throws IOException {
  Scalar<Long> length = new of(() -> lengthOf(id));
  return length.value() / MAX_SCORE;
}

private long lengthOf(CurrencyId id) throws IOException {
  ListIterable<String> iterable = new IoChecked<>(
    () -> new Files(new AbsPath(id.value())).iterate()
  );
  return new LengthOf(iterable).longValue();
}
```

In this patch, we replace the usage of the deprecated `LengthOf` class with a new method `lengthOf` that uses a different approach to calculate the length of a file. The new method uses the `LengthOf` class from the `cactoos` library, which is an alternative to the deprecated class.

Note that this patch assumes that the `IoChecked` and `Files` classes are available in the classpath. If these classes are not available, you may need to modify the patch accordingly.