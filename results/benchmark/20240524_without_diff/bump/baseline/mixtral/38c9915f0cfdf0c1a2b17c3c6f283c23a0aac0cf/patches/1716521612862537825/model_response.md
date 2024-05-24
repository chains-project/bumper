Here is the proposed patch:

```java
import org.cactoos.text.UncheckedText;
import org.cactoos.text.TextOf;

// ...

public RtTransaction(String id, String hash, long timestamp, String from,
    String to, String amount, String fee, String signature,
    String nonce, String version, String type, String status,
    String data, String[] logs) {
    super(
        new TextOf(id),
        new TextOf(hash),
        new TextOf(timestamp),
        new UncheckedText(from),
        new UncheckedText(to),
        new UncheckedText(amount),
        new UncheckedText(fee),
        new UncheckedText(signature),
        new UncheckedText(nonce),
        new UncheckedText(version),
        new UncheckedText(type),
        new UncheckedText(status),
        new UncheckedText(data),
        new TextOf(logs)
    );
}
```

The patch replaces the usage of `TrimmedText` with `UncheckedText` and `TextOf` to handle the string inputs.