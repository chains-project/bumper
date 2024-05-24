Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double rtScore(String input) throws IOException {
    return new LengthOf<String>(input).longValue();
}
```
Explanation:

* I changed the import statement to use `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`.
* I updated the method to use the new `LengthOf` constructor that takes a `String` as input and returns a `Long`.
* I then called the `longValue()` method to convert the `Long` to a `double`.