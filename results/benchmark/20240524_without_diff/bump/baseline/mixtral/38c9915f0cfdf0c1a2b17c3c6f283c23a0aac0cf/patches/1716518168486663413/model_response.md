Here's the fixed version of the failing code:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(TransactionInput input, TransactionOutput output,
    TransactionSigner signer, TransactionVerifier verifier,
    TransactionIdSupplier idSupplier, TransactionDb db) {
    super(input, output, signer, verifier, idSupplier, db);
    this.amount = new UncheckedText(input.amount());
    this.fee = new UncheckedText(input.fee());
    this.hash = new TextEnvelope(input.hash(), "SHA-256");
    this.timestamp = new UncheckedText(input.timestamp());
    this.publicKey = new UncheckedText(input.publicKey());
}
```

The changes include importing the necessary classes and wrapping the input parameters that were previously using the removed `TrimmedText` class with either `UncheckedText` or `TextEnvelope` to match the available classes in the new library version.