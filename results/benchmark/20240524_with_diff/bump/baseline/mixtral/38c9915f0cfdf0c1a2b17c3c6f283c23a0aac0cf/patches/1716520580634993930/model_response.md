Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtApi api, RtDb db, RtUser user, String hash) {
  this.api = api;
  this.db = db;
  this.user = user;
  this.hash = hash;
  this.len = new LengthOf<RtObject>(db.objects());
}
```
In this patch, I replaced the import statement to use `LengthOf` from `org.cactoos.scalar` package, which is a new addition in the library version. The `LengthOf` instance is created using `db.objects()` instead of `db.iterator()` to match the new method signature.