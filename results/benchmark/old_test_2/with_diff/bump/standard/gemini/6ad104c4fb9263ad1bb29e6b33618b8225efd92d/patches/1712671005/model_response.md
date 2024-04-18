```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public ChachaDecoder() {
        AlertDescription alertDescription = new TlsFatalAlert(AlertDescription.internal_error).getAlertDescription();
    }
}
```