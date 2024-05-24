Here's the patched version of the client code:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(RtUser user, RtAmount amount, RtTimestamp timestamp,
    RtSignature signature, RtHash hash, RtProof proof) {
  this.user = user;
  this.amount = amount;
  this.timestamp = timestamp;
  this.signature = signature;
  this.hash = hash;
  this.proof = proof;
  this.id = new TextOf(
      new UncheckedText(
          String.format("%s:%s:%s:%s:%s:%s",
              user.asString(),
              amount.asString(),
              timestamp.asString(),
              signature.asString(),
              hash.asString(),
              proof.asString()
          )
      )
  ).asString();
}
```

In this patched version, I replaced the `TrimmedText` import with `TextOf` and `UncheckedText` imports. Also, I replaced the `trimmed()` method call with a `TextOf` constructor that takes a `CharSequence` parameter and an `UncheckedText` constructor that takes a `CharSequence` parameter. This way, the code now uses the `TextOf` and `UncheckedText` classes from the new library version instead of the removed `TrimmedText` class.