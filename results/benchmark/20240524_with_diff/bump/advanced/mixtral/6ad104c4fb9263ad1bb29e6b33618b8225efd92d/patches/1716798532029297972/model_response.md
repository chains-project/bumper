Here's the fixed `ChachaDecoder.java` method with the required import statement for the new library version:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void decode(TlsContext context, InputStream input) throws IOException {
    // ...
    try {
        // ...
    } catch (Exception ex) {
        // ...
        throw new TlsFatalAlert(AlertDescription.internal_error);
    }
}
```

The `TlsFatalAlert` constructor now requires an `AlertDescription` parameter instead of a short value.