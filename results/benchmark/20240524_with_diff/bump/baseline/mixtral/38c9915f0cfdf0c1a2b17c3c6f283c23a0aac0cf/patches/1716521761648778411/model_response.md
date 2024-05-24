Here is a proposed patch for the failing client code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtTxId id, RtTxData data) {
  this.env = env;
  this.id = id;
  this.data = data;
  this.length = new LengthOf(data.asIterable());
}
```
In this patch, we have imported the new `LengthOf` class from the `org.cactoos.scalar` package instead of the old `org.cactoos.iterable` package. We have also updated the argument to the `LengthOf` constructor to be the `Iterable` returned by the `data.asIterable()` method. This should allow the code to compile with the new version of the library.