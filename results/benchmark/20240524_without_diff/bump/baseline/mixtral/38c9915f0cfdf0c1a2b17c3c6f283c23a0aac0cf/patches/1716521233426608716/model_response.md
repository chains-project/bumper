Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String input) throws IOException {
  // Use the new method in the updated library
  LengthOf length = new LengthOf(input);
  return length.intValue();
}
```
In this patch, I replaced the old `LengthOf` import with the new one from the updated library. I also replaced the usage of `LengthOf` with the new method that accepts a `java.lang.String` as its parameter.