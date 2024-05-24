Here's the fixed version of the client code that uses the new `BytesOf` method instead of the removed `TrimmedText`:

```java
import org.cactoos.text.BytesOf;

// ...

public RtTransaction(String id, String hash, long timestamp, String from, String to, Long amount, String fee, String nonce, String signature) {
    this.id = id;
    this.hash = hash;
    this.timestamp = timestamp;
    this.from = new BytesOf(from); // use BytesOf instead of TrimmedText
    this.to = to;
    this.amount = amount;
    this.fee = fee;
    this.nonce = nonce;
    this.signature = signature;
}
```
In this version, the `from` parameter is converted to a `BytesOf` object instead of a `TrimmedText` object. This should fix the compilation error caused by the removal of the `TrimmedText` class.