Here's a possible patch for the failing client code:

```java
import org.cactoos.scalar.LengthOf;

// ...

public double rtScore(String input) throws IOException {
  long length = new LengthOf<String>(input).intValue();
  // ...
}
```

In this patch, we replaced the import statement to use the new `LengthOf` class in the `org.cactoos.scalar` package. We also changed the type of the `length` variable to `long`, and called the `intValue()` method to get the length as an `int`. Note that the behavior of the method is unchanged, so it should still produce the same output as before.