Here is a proposed patch for the failing method:
```java
import org.bouncycastle.crypto.tls.TlsAlert;

// ...

public void decodeHandshakeMessage(InputStream input, HandshakeMessage handshakeMessage) throws IOException {
    // ...

    int alertDescription = input.read();
    TlsAlert tlsAlert = new TlsAlert(TlsFatalAlert.INTERNAL_ERROR, AlertDescription.decode(alertDescription));

    // ...
}
```
Note that I have imported the `TlsAlert` class instead of `TlsFatalAlert` and used it to create a new TLS alert with the appropriate alert description. This should fix the error caused by the removal of the `TlsFatalAlert` constructor.