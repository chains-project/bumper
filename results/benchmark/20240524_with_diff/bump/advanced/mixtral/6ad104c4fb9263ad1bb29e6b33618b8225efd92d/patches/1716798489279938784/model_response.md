Here's the patched version of the failing method in `ChachaDecoder.java`. I've imported the new class `TlsFatalAlert` and used its constructor with `short` argument.

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ... (other imports and class definition)

private void decode(ByteBuffer input, ByteBuffer output) throws IOException {
    try {
        // ... (other code)

        if (tag != TAG_AEAD_DATA) {
            throw new TlsFatalAlert(AlertDescription.decryption_failed);
        }

        // ... (other code)
    } catch (TlsFatalAlert ex) {
        // ... (other code)
    }
}
```

This patch replaces the old constructor `TlsFatalAlert(short)` with the new fully qualified constructor `TlsFatalAlert(AlertDescription)`. The `AlertDescription` enum provides a constant `decryption_failed` that can be used instead of the raw `short` value.