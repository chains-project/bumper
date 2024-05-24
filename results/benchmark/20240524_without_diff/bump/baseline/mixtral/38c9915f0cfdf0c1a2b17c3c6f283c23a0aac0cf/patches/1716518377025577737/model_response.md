Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtUser user, RtItem item, long amount, byte[] data) {
  this.env = env;
  this.user = user;
  this.item = item;
  this.amount = amount;
  this.data = data;
  this.id = new LengthOf<RtItem>(item).intValue();
}
```
In this patch, I replaced the usage of `LengthOf` from `org.cactoos.iterable` with the new `LengthOf` from `org.cactoos.scalar`. This change allows the code to compile with the new library version.