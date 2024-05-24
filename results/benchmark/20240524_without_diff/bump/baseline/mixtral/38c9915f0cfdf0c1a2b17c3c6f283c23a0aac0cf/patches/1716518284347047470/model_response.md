Here is the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtId id, RtAmount amount, RtProof proof) {
  this.env = env;
  this.id = id;
  this.amount = amount;
  this.proof = proof;
  this.len = new LengthOf<>(id.asIterable());
}
```
In this patch, I replaced the import statement to use the new `LengthOf` class in the `org.cactoos.scalar` package. I also changed the type of the `len` field from `int` to `LengthOf`, and initialized it with the new `LengthOf` constructor that takes an `Iterable` argument.