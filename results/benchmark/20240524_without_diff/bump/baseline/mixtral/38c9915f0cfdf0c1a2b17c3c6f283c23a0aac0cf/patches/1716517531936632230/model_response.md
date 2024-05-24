Here's the suggested patch to fix the error:

```java
import org.cactoos.bytes.IoCheckedBytes;
import java.nio.charset.StandardCharsets;

// ...

import static java.util.stream.Collectors.joining;

// ...

private String asString(Bytes source) {
    return new IoCheckedBytes(source, StandardCharsets.UTF_8.name())
      .asBytes()
      .stream()
      .mapToObj(Byte::toString)
      .collect(joining());
}
```

The patch replaces the usage of `IoCheckedScalar` with `IoCheckedBytes`, which is a new class added in the updated library version. The `asString` method is updated to read the bytes and convert them to a string.