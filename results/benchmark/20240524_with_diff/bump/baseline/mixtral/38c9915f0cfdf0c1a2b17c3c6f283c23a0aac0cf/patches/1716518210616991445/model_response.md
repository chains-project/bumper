Here is the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtDb db, RtApi api, RtUser user, RtAmount amount, RtProof proof) {
  this.db = db;
  this.api = api;
  this.user = user;
  this.amount = amount;
  this.proof = proof;
  this.id = new LengthOf<>(db.list(user.id())).intValue();
  this.created = new LengthOf<>(db.list(user.id(), Timestamp.format())).intValue();
}
```
In this patch, I replaced the `org.cactoos.iterable.LengthOf` class with the `org.cactoos.scalar.LengthOf` class, which is a new addition in the updated library version. This should resolve the "cannot find symbol" error.