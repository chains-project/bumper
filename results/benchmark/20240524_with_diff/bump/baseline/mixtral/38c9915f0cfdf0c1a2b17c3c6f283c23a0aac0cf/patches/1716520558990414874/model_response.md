Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtTxId id, RtTxData data) {
  this.env = Objects.requireNonNull(env);
  this.id = Objects.requireNonNull(id);
  this.data = Objects.requireNonNull(data);
  this.len = new LengthOf<CharSequence>(this.data.toString());
}
```
In this patch, I replaced the usage of `org.cactoos.iterable.LengthOf` with `org.cactoos.scalar.LengthOf` since the former was removed and the latter was added in the new library version. The `LengthOf` from `org.cactoos.scalar` returns a `Scalar` instead of an `Iterable`, so I changed the type of the `len` variable accordingly.