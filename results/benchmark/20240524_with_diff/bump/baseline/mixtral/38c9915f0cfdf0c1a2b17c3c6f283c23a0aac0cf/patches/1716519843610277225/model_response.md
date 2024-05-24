Here's a patch that you can apply to fix the error:

```java
import org.cactoos.scalar.LengthOf;

// ...

@Override
public double scoreOf(RtValue value) {
  return new LengthOf(value.asIterable()).value();
}
```

In the patched code, I replaced the old `LengthOf` import with the new one from the `org.cactoos.scalar` package. The `scoreOf` method now uses the new `LengthOf` class to calculate the length of the input iterable, which should resolve the "cannot find symbol" error.