Here's the proposed patch:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

//...

public RtTransaction(String id, String hash, String data, Long time, Long nonce,
        String from, String to, Long amount, String fee, String signature,
        String txType, String version, String... tags) {
    //...
    this.id = new UncheckedText(id);
    this.hash = new UncheckedText(hash);
    this.data = new UncheckedText(data);
    this.time = new TextOf(time);
    this.nonce = new TextOf(nonce);
    this.from = new UncheckedText(from);
    this.to = new UncheckedText(to);
    this.amount = new TextOf(amount);
    this.fee = new TextOf(fee);
    this.signature = new UncheckedText(signature);
    this.txType = new UncheckedText(txType);
    this.version = new UncheckedText(version);
    if (tags != null) {
        this.tags = new TextOf(Arrays.asList(tags));
    } else {
        this.tags = new TextOf(Collections.emptyList());
    }
}
```

In this patch, I replaced all instances of `TrimmedText` with `UncheckedText` and `TextOf` to fix the compilation error. The `UncheckedText` class is a drop-in replacement for `TrimmedText` and provides similar functionality. I also used `TextOf` to convert primitive values and collections to `Text`.