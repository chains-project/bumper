Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtStore store, RtUser user, RtAmount amount, RtProof proof, RtComment comment) {
  this.store = store;
  this.user = user;
  this.amount = amount;
  this.proof = proof;
  this.comment = comment;
  this.id = new LengthOf<RtProof>(proof).intValue();
}
```
The only change is importing `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`. The `LengthOf` class was moved from the `iterable` package to the `scalar` package in the new library version.