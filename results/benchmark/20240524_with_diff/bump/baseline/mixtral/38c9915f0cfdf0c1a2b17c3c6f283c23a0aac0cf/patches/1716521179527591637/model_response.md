Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String id) throws IOException {
  try (Input input = api().input(id)) {
    return new LengthOf(input).intValue();
  }
}
```
Explanation:
The error message indicates that the `LengthOf` class cannot be found in the `org.cactoos.iterable` package. According to the library changes, the `LengthOf` class has been moved to the `org.cactoos.scalar` package. Therefore, we need to import it from the new package.
The original code uses the `LengthOf` class to calculate the length of an iterable. However, in the new library version, the `LengthOf` class is used for scalar values, such as `Input`. Therefore, we can modify the code to use the `LengthOf` class with the `Input` instance.
Note that I changed the return type from `long` to `double` to match the return type of the original method. If you want to keep the original return type, you can simply cast the result to `long`.