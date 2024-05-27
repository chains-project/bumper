```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public TlsFatalAlert getAlertDescription(short alertDescription) {
        return new TlsFatalAlert(alertDescription);
    }
}
```