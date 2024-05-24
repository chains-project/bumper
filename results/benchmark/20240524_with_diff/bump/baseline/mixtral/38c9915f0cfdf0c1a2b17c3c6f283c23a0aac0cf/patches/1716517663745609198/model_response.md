Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double rtScore(String input) throws ApiException {
    InputStream in = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
    return new LengthOf(new IterableOf(in)).longValue();
}
```
In this patch, we've imported the new `LengthOf` class from `org.cactoos.scalar` and used it to calculate the length of the input. The `IterableOf` class is used to convert the input stream to an iterable, which is accepted by the new `LengthOf` class.