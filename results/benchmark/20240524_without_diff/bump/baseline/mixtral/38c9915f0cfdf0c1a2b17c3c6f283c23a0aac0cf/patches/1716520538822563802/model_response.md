Here is the proposed patch:

```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtTxId id, RtAmount amount, RtSign sign,
    RtUser user, RtHash hash, RtTime time) {
    this.env = env;
    this.id = id;
    this.amount = amount;
    this.sign = sign;
    this.user = user;
    this.hash = hash;
    this.time = time;
    this.len = new LengthOf<>(this.id.value());
}
```

The only change made is to import `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`. This is because the `LengthOf` class has been moved from the `iterable` package to the `scalar` package. The rest of the code remains unchanged.