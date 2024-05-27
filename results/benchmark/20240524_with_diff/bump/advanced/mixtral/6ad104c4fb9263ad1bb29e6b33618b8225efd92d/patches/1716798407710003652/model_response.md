Here's a fixed version of the failing method in `ChachaDecoder.java`. Note that since `TlsFatalAlert` constructor is removed, I replaced it with a new exception constructor `IllegalStateException`. Also, I replaced `TlsFatalAlert.getAlertDescription()` with a new static method `AlertDescription.getAlertDescription(short)`.

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import java.io.IOException;

public void decodeRecord(InputStream in, OutputStream out) throws IOException {
    try {
        // ... (previous code)

        if (type == Type.alert) {
            int alertDescription = in.readUnsignedShort();
            throw new IllegalStateException(String.format("TLS Alert: %s", AlertDescription.getAlertDescription(alertDescription)));
        }

        // ... (remaining code)
    } catch (TlsFatalAlert ex) {
        throw new TlsFatalAlertException(ex.alertDescription);
    }
}
```