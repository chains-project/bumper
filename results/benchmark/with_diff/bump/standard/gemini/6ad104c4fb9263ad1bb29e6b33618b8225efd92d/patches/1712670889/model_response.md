```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public ChachaDecoder(TlsFatalAlert alert) {
        if (alert.getAlertDescription() != AlertDescription.close_notify) {
            throw new IllegalStateException("Unexpected alert: " + alert.getAlertDescription());
        }
    }
}
```