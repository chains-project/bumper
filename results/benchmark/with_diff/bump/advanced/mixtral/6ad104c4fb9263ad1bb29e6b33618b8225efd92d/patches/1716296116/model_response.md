Here's the proposed patch for the `ChachaDecoder.java` file:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void decodeHandshakeMessage() {
    // ...

    try {
        // ...

        if (contentType != ContentType.handshake) {
            throw new TlsFatalAlert(AlertDescription.unexpected_message);
        }

        // ...

    } catch (IOException e) {
        throw new TlsFatalAlert(AlertDescription.decode_error);
    }
}
```

The patch adds a new import for the `TlsFatalAlert` class. Also, the `TlsFatalAlert` constructor with a single short argument has been removed, so we now use the `TlsFatalAlert(AlertDescription)` constructor instead.