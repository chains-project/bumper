```java
import org.bouncycastle.crypto.tls.AlertLevel;
import org.bouncycastle.crypto.tls.ProtocolVersion;

public class ChachaDecoder {

    public void decode(byte[] buf, int off, int len, ProtocolVersion version) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertLevel.fatal, AlertDescription.decode_error);
        }

        // Create a new TlsFatalAlert object using the added constructor
        TlsFatalAlert alert = new TlsFatalAlert(AlertDescription.decode_error);

        // Throw the alert using the original method signature
        throw alert;
    }
}
```