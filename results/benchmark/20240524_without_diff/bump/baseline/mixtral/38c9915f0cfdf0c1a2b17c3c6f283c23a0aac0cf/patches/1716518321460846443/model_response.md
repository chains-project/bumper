Here's a proposed patch for the failing client code:

```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(String hash) {
  this.hash = hash;
  this.length = new LengthOf<>(inputOf(hash));
}
```

In this patch, we changed the import statement to import `LengthOf` from the `org.cactoos.scalar` package instead of `org.cactoos.iterable`. We also changed the type of the `length` field from `LengthOf<Iterable>` to `LengthOf<Input>`.

Note that the `LengthOf` constructor with an `Input` parameter was added in the new library version, so we can safely use it. Also, since the `LengthOf` class now extends `ScalarEnvelope` instead of `IterableEnvelope`, we need to change the type of the `length` field accordingly.