Here's the proposed patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoCheckedBytes;
import org.cactoos.io.InputOf;
import org.cactoos.text.TextOf;

// ...

public class RtNetwork {
  // ...

  @Override
  protected String name() throws IOException {
    Scalar<String> scalar = () -> new TextOf(
      new IoCheckedBytes(
        new InputOf(new URL(url())),
        IoCheckedBytes::asBytes
      )
    ).asString();
    return scalar.value();
  }
}
```

This patch replaces the usage of `IoCheckedScalar` with a combination of `IoCheckedBytes`, `InputOf`, and `TextOf` classes. The `IoCheckedBytes` class is used to read the contents of the URL, and then it is converted to a string using the `TextOf` class. The `Scalar` interface is used to create a lazily evaluated object that can be used with the existing code.