Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtApi api, RtDb db, RtUser user, String hash) {
  this.api = api;
  this.db = db;
  this.user = user;
  this.hash = hash;
  this.txs = new LengthOf<>(db.list(user.id(), hash));
}
```
The only change is importing `LengthOf` from `org.cactoos.scalar` instead of `org.cactoos.iterable`. This is because the `LengthOf` class has been moved from `org.cactoos.iterable` to `org.cactoos.scalar` in the new library version.