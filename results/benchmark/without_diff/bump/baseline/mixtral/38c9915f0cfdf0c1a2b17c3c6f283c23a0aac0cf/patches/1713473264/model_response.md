Here's a patch that you can apply to fix the error:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.Joined;

// ...

@Override
public TextEnvelope<String> valuesOf(String name) throws IOException {
  List<String> values = new ArrayList<>();
  try (Stream<String> lines = Files.lines(Paths.get(dataPath(name)))) {
    lines.forEach(values::add);
  }
  return new Joined<>("\n", values);
}
```

In this patch, we replaced the usage of `JoinedText` with `Joined`, which is a part of the same library (Cactoos) and provides similar functionality. Additionally, we replaced the `TextEnvelope` implementation from `TextEnvelope.String` to `TextEnvelope`, which is a more general implementation in the same library.