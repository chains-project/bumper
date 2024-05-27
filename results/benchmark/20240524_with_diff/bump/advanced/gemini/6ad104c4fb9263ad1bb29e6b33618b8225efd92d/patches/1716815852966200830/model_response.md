```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public ChachaDecoder(TlsFatalAlert alert) {
        if (alert.getAlertDescription() != AlertDescription.internal_error) {
            throw new RuntimeException("Invalid alert description: " + alert.getAlertDescription());
        }
    }
}
```