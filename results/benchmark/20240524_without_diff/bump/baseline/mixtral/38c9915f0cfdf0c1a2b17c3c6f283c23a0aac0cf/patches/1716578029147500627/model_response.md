Here's a patch that you can apply to the code in order to fix the error:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.Joined;

// ...

@Override
public TextEnvelope<Double> values() throws IOException {
  return new Joined<Double>(", ", input.values());
}
```

This patch replaces the failing import statement with the correct one, and modifies the `values()` method to use the `Joined` class from the updated library version. The `TextEnvelope` interface is used instead of the raw `Double` type for consistency with the method's signature.