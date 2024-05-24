Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtInput input) {
  this.input = new LengthOf(input.stream());
  // ...
}
```
In this patch, I replaced the import statement to use `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`. I also changed the instantiation of `this.input` to use `LengthOf` with the stream of `input`. This way, the code can work with the new version of the library.