Sure, here's a proposed patch for the failing client code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double rtScore(String input) throws IOException {
  long start = System.nanoTime();
  double result = new LengthOf(new IoInput(input)).longValue();
  long finish = System.nanoTime();
  // ...
}
```
In this patch, we've imported the new `LengthOf` class from the `org.cactoos.scalar` package, which is an added method in the new library version. We've also updated the `LengthOf` constructor to take an `IoInput` object as its argument, which is a new class that wraps a string input. Finally, we've updated the `longValue()` method call to match the new method signature.