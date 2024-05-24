Here's the proposed patch:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String id, String hash, Long timestamp, Long nonce,
    TextEnvelope<Long> amount, TextEnvelope<Long> fee, TextEnvelope<Long> balance,
    TextEnvelope<String> from, TextEnvelope<String> to, TextEnvelope<String> signature,
    TextEnvelope<String> data) {
    super(
        new UncheckedText(id),
        new UncheckedText(hash),
        new UncheckedText(timestamp.toString()),
        new UncheckedText(nonce.toString()),
        new UncheckedText(amount.asString()),
        new UncheckedText(fee.asString()),
        new UncheckedText(balance.asString()),
        new UncheckedText(from.asString()),
        new UncheckedText(to.asString()),
        new UncheckedText(signature.asString()),
        new UncheckedText(data.asString())
    );
}
```

The patch introduces a new import statement for `TextEnvelope` and `UncheckedText` classes. The `TrimmedText` class has been removed, so we replace it with `UncheckedText` which does not trim the text. Also, we use `TextEnvelope` to wrap `Long` values as text, instead of directly converting them to `Text` using `TextOf`. This is because `TextOf` constructor that accepts a `Long` has been removed.

Note: I assumed that the `RtTransaction` constructor takes `TextEnvelope` instead of `TrimmedText`. If that's not the case, you may need to adjust the code accordingly.