```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public ChachaDecoder(TlsFatalAlert fatalAlert) {
        if (fatalAlert.getAlertDescription() != AlertDescription.close_notify) {
            throw fatalAlert;
        }
    }
}
```