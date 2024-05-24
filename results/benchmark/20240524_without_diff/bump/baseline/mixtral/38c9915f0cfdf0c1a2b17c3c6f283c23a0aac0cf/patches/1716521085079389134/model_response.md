Here's a possible patch to fix the error:

```java
import org.cactoos.bytes.IoCheckedBytes;
import java.nio.charset.StandardCharsets;

// ...

IoCheckedScalar<String> scalar = new IoCheckedScalar<>(
  () -> new IoCheckedBytes(
    () -> this.in.body().bytes(),
    StandardCharsets.UTF_8.name()
  ).asBytes()
);
```

This code creates a new `IoCheckedScalar` that reads the body of the `in` object as bytes, then converts those bytes to a string using the specified character set. The `IoCheckedBytes` class is a new addition in the updated library version.