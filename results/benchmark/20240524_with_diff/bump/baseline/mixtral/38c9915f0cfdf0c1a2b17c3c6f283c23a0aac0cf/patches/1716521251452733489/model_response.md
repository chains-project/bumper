Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String userId) throws IOException {
  try (InputStream in = new URL(baseUrl + "/users/" + userId).openStream()) {
    return new LengthOf(in).longValue();
  }
}
```
Explanation:
The `LengthOf` class was moved from `org.cactoos.iterable` to `org.cactoos.scalar`. Additionally, the constructor signature has changed to accept an `Iterable` or `Input` instead of `Iterable`. Therefore, we need to update the import statement and modify the code to use the new constructor that accepts an `Input` parameter.