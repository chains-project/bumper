Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtTransactions parent, String id) {
  this.parent = parent;
  this.id = id;
  this.length = new LengthOf(parent.list(id));
}
```
In this patch, I replaced the `org.cactoos.iterable.LengthOf` with `org.cactoos.scalar.LengthOf` since the former was removed and the latter was added in the new library version. This change allows the code to compile and work correctly.