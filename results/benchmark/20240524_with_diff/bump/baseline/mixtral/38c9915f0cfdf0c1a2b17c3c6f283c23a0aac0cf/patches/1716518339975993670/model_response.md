Here is the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtTxIn in, RtTxOut out, RtTxLog log) {
  this.env = env;
  this.in = new LengthOf<>(in);
  this.out = out;
  this.log = log;
}
```
In this patch, we import `LengthOf` from `org.cactoos.scalar` instead of `org.cactoos.iterable`. We also change the type of the `in` field from `RtTxIn` to `LengthOf<RtTxIn>`. This allows us to use the new `LengthOf` constructor that takes an `Iterable` as its argument.