Here's the proposed patch for the `ChachaDecoder.java` file:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void decodeHandshakeMessage(InputStream input) throws IOException {
    // ...

    try {
        // ...
    } catch (TlsFatalAlert ex) {
        throw new TlsFatalAlert(ex.getAlertDescription());
    }
}
```

The patch adds an import for `TlsFatalAlert` and replaces the caught exception type from `Exception` to `TlsFatalAlert`. The `TlsFatalAlert` constructor with a single `AlertDescription` parameter has been added in the new library version, so it can be used here. The `getAlertDescription()` method is still available, so it can be used to keep the same behavior as before.