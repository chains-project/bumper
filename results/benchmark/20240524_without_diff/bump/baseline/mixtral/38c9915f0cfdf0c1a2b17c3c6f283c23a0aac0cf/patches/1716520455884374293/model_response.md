Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(String id, RtAccount from, RtAccount to, RtValue amount, RtValue fee, RtValue timestamp) {
  this.id = id;
  this.from = from;
  this.to = to;
  this.amount = amount;
  this.fee = fee;
  this.timestamp = timestamp;
  this.valid = LengthOf.lengthOf(from.iterableIds()).intValue() > 0;
}
```
In this patch, I replaced the `org.cactoos.iterable.LengthOf` with `org.cactoos.scalar.LengthOf`. This is possible because the new version of the library includes a method `public LengthOf org.cactoos.scalar.LengthOf(java.lang.Iterable)` which can be used to get the length of an iterable.