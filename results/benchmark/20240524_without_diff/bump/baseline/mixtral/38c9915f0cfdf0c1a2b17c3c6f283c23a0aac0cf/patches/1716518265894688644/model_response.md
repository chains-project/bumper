Here's the fixed version of the code that uses the new `LengthOf` method from the updated library:

```java
import org.cactoos.scalar.LengthOf;

// ...

@Override
public RtTransaction withId(String id) {
  this.id = new LengthOf(id).intValue();
  return this;
}
```

In the updated library, the `LengthOf` class is now located in the `org.cactoos.scalar` package, and it accepts an `Iterable` or `Input` as a constructor argument. In this case, we can use the `LengthOf` constructor that accepts a `String` argument, since a `String` is an `Iterable` of characters.