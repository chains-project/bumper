Here is the proposed patch:
```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String id, String hash, Long nonce, Text value, Text fee, Text timestamp, Text signature) {
  this.id = new UncheckedText(id);
  this.hash = new UncheckedText(hash);
  this.nonce = new UncheckedText(nonce.toString());
  this.value = new TextOf(value);
  this.fee = new TextOf(fee);
  this.timestamp = new TextOf(timestamp);
  this.signature = new UncheckedText(signature);
}
```
Explanation:
In the original code, the constructor of `RtTransaction` takes a `Text` object as the value of the transaction. However, the updated library version no longer has the `Text` class. Instead, it has a method `TextOf` that can convert a `CharSequence` to a `Text` object. Therefore, we can use the `TextOf` method to convert the `value`, `fee`, `timestamp`, and `signature` parameters to `Text` objects.

Note that I added the import statements for `TextOf` and `UncheckedText` at the beginning of the code. I also changed the `Text` object to `UncheckedText` for the `id`, `hash`, `nonce`, and `signature` parameters since they are not coming from user input and are guaranteed to be non-null.