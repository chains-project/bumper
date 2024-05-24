Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(String id, Input input) {
  this.id = id;
  this.input = new LengthOf(input);
  // ...
}
```
The only change made is importing `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`. The rest of the code remains unchanged.