Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtId id, RtItem item, int amount, RtCredit credit,
    RtDebit debit, RtDelta delta, RtHash hash, RtTimestamp timestamp, RtSign sign) {
  this.env = env;
  this.id = id;
  this.item = item;
  this.amount = amount;
  this.credit = credit;
  this.debit = debit;
  this.delta = delta;
  this.hash = hash;
  this.timestamp = timestamp;
  this.sign = sign;
  this.length = new LengthOf<RtItem>(item); // use the new LengthOf method
}
```
In the above patch, I replaced the old `LengthOf` method from `org.cactoos.iterable` with the new `LengthOf` method from `org.cactoos.scalar`. The new `LengthOf` method takes an `Iterable` as a parameter, which is compatible with the `RtItem` class.