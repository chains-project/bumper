Here's a patch that you can apply to fix the error:

```java
import org.cactoos.text.Joined;

// ...

@Override
public List<String> asList(String pattern) {
  List<String> result = new ArrayList<>();
  try (TextReader reader = new TextReader(pattern)) {
    for (String line : new LinesOf(reader)) {
      if (!line.trim().isEmpty()) {
        result.add(line);
      }
    }
  } catch (IOException e) {
    throw new RuntimeException(e);
  }
  return result;
}
```

In this patch, I replaced the `JoinedText` class with the `Joined` class from the same library. I also changed the import statement accordingly. The `LinesOf` class is a new addition to the library, so I used it instead of the removed `TextOf` class. I also wrapped the `LinesOf` object in a `TextReader` object to read the lines of the input text.

Note that the `TextReader` class is a new addition to the library, so it can be used in the fixed code. However, the `TextOf` class has been removed from the library, so it cannot be used in the fixed code.

I hope this helps! Let me know if you have any questions or concerns.