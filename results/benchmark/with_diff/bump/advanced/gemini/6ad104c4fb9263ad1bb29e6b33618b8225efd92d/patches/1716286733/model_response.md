```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public ChachaDecoder(TlsFatalAlert fatalAlert) {
        if (fatalAlert.getAlertDescription() == AlertDescription.bad_record_mac) {
            throw new RuntimeException("Bad record MAC");
        }
    }
}
```