Here is the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double score(String input) throws IOException {
    return new LengthOf(Iterables.iterate(input)).value();
}
```
In this patch, I replaced the import statement to use the new `LengthOf` class in the `org.cactoos.scalar` package. I also changed the method to use the new `LengthOf` constructor that takes an `Iterable` parameter. Finally, I called the `value()` method instead of the `longValue()` method, since the new `LengthOf` class returns a `Scalar` instead of a `Long`.