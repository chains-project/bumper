Here's a patch that you can apply to the failing client code:

```java
import org.cactoos.scalar.Scalar;
import org.cactoos.scalar.UncheckedScalar;

// ...

import static org.cactoos.TextOfScalar.textOf;

// ...

Scalar<String> solidScalar = new UncheckedScalar<String>(() -> "your-value-here");
String value = textOf(solidScalar).asString();
```

This code creates a new `UncheckedScalar` instance that wraps a lambda expression that returns the desired value. Then, it creates a new `TextOfScalar` instance that converts the `UncheckedScalar` to a `Text` instance. Finally, it extracts the value as a string using the `asString()` method.

Note that you need to replace the string "your-value-here" with the actual value that you want to use.