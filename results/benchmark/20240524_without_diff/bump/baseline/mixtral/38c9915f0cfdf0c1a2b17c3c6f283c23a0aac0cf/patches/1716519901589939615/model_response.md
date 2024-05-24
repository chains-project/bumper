Sure, here's the fixed version of the failing code using the new `LengthOf` method from `org.cactoos.scalar` package:
```java
import org.cactoos.scalar.LengthOf;

// ...

@Override
public double score(User user) throws IOException {
  return new LengthOf(user.feed()).value();
}
```
In this code, `user.feed()` returns an `Iterable` of `byte[]`, so we can use `LengthOf` from `org.cactoos.scalar` to get the length of the feed.

Note that I had to make an assumption that `user.feed()` returns an `Iterable` of `byte[]`, since the original code was not provided. If this assumption is incorrect, you may need to adjust the argument to `LengthOf` accordingly.