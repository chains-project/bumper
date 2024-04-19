Here's a proposed patch for the failing client code:

```java
import org.cactoos.text.Texts;

// ...

@Override
public String join(List<String> urls) throws IOException {
  return new JoinedText(Texts.safe(urls), "\n").asString();
}
```

This patch replaces the usage of the removed `JoinedText` constructor with the equivalent constructor from the `Texts` class, which was added in the new library version. The `Texts.safe` method is used to safely convert the list of URLs to a list of `Text` objects, which can then be joined using the `JoinedText` constructor. The `asString` method is then called on the `JoinedText` object to get the final string.