Here's the fixed version of the failing method using the `Joined` class from the `org.cactoos.iterable` package, which is a replacement for the removed `JoinedText` class:

```java
import org.cactoos.iterable.IterableOf;
import org.cactoos.text.Joined;

// ...

@Override
public String format(Map<String, String> map) {
  return new Joined("\n", new IterableOf<String>(
    () -> map.entrySet().stream()
      .map(entry -> String.format("%s: %s", entry.getKey(), entry.getValue()))
      .toArray(String[]::new)
  )).asString();
}
```

The `Joined` class takes an iterable of strings and joins them using a specified separator. Here, we use an `IterableOf` to create an iterable from a stream of entries in the input map. Each entry is formatted as a string and added to the iterable. Finally, the `Joined` class is used to join the resulting iterable into a single string.