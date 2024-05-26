```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public ChachaDecoder(TlsFatalAlert alert) {
        if (alert.getAlertDescription() != TlsFatalAlert.BAD_CERTIFICATE) {
            throw alert;
        }
    }
}
```