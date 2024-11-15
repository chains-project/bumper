Here's the proposed patch:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String id, String hash, Long nonce, Long amount,
    Long fee, Long timestamp, String sender, String recipient,
    String signature, Status status) {
    this.id = new UncheckedText(id);
    this.hash = new UncheckedText(hash);
    this.nonce = new UncheckedText(nonce.toString());
    this.amount = new UncheckedText(amount.toString());
    this.fee = new UncheckedText(fee.toString());
    this.timestamp = new UncheckedText(timestamp.toString());
    this.sender = new UncheckedText(sender);
    this.recipient = new UncheckedText(recipient);
    this.signature = new UncheckedText(signature);
    this.status = status;

    this.amountInCents = new TextOf(amount.multiply(CENTS_IN_DOLLAR));
}
```

The patch replaces the usage of `TrimmedText` with `UncheckedText` and `TextOf` classes from the updated library version.