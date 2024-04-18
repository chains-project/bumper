Here's the fixed version of the failing method using the `Joined` class from the `org.cactoos.iterable` package, which is a replacement for the removed `JoinedText` class:

```java
import org.cactoos.iterable.IterableOf;
import org.cactoos.text.Joined;

// ...

@Override
public String asString() throws IOException {
  return new Joined(new IterableOf<Text>(
    new TextOf(new WalletsJson(new WalletsIn(this.api()))),
    "\n"
  )).asString();
}
```
This code creates a new `IterableOf` object containing a single `TextOf` object, which converts the `WalletsJson` object to a `Text` object. The `"\n"` string is also added to the iterable as a separator between the two texts. The `Joined` object then concatenates the two texts together with the separator, producing the final string.