```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public ChachaDecoder(TlsFatalAlert alert) {
        if (alert.getAlertDescription() != AlertDescription.unexpected_message) {
            throw new IllegalStateException("Unexpected alert: " + alert.getAlertDescription());
        }
    }
}
```