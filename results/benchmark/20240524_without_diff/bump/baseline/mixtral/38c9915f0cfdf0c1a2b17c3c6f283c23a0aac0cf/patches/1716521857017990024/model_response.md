Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, byte[] data, RtUser user) {
  this.env = env;
  this.data = data;
  this.user = user;
  this.len = new LengthOf<byte[]>(data).intValue();
}
```
In this patch, I replaced the usage of the removed `LengthOf` method from `org.cactoos.iterable` with the new `LengthOf` method from `org.cactoos.scalar`. The new method takes an `Iterable` or an `Input` as its argument, and both `byte[]` and `data` are compatible with these types.