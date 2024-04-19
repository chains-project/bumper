Here is a possible patch for the failing client code:
```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.TextJoined;

// ...

@Override
public String join(List<String> ids) throws IOException {
  return new TextJoined(",", new TextEnvelope<String>() {
    @Override
    protected String textOf(String id) {
      return id;
    }
  }).asString(ids);
}
```
Explanation:
The `JoinedText` class has been removed in the new library version, and replaced by the `TextJoined` class.
The `TextJoined` class requires a `TextEnvelope` instead of a `CharSequence` as input.
Therefore, we need to create a `TextEnvelope` that converts the input `String` to a `CharSequence`.
This can be done by creating an anonymous inner class that implements the `TextEnvelope` interface and overrides the `textOf` method.
The `textOf` method simply returns the input `String` as a `CharSequence`.
Finally, we can use the `TextJoined` class to join the input `List<String>` with a comma separator and return the result as a `String`.