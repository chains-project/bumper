Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtTxId id, RtTxData data) {
  this.env = Objects.requireNonNull(env);
  this.id = Objects.requireNonNull(id);
  this.data = Objects.requireNonNull(data);
  this.length = new LengthOf<String>(data.asJson()).intValue();
}
```
In this patch, I replaced the old `LengthOf` import from `org.cactoos.iterable` with the new `LengthOf` import from `org.cactoos.scalar`. The `LengthOf` class now expects an `Iterable` or `Input` as its constructor argument, so I wrapped the `data.asJson()` return value with `<String>` to make it compatible with the new `LengthOf` constructor.