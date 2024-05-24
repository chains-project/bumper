Here's a possible patch for the client code:
```java
import org.cactoos.text.BytesOf;
import org.cactoos.text.UncheckedText;

...

public RtTransaction(String id, String hash, String data, Long nonce,
  TransactionType type, Long amount, Long fee, Long timestamp,
  PublicKey sender, PublicKey receiver, Signature signature)
    throws IOException, CryptoException
{
  this.id = new UncheckedText(id);
  this.hash = new UncheckedText(hash);
  this.data = new BytesOf(new UncheckedText(data));
  this.nonce = nonce;
  this.type = type;
  this.amount = amount;
  this.fee = fee;
  this.timestamp = timestamp;
  this.sender = sender;
  this.receiver = receiver;
  this.signature = signature;
  this.validate();
}
```
In this patch, I replaced the use of `SplitText` with `BytesOf` and `UncheckedText` to convert the `data` parameter to a `Bytes` object. This way, the code can work with the new version of the library.