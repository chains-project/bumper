```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public static TlsFatalAlert createFatalAlert(short alertDescription) {
        return new TlsFatalAlert(alertDescription);
    }
}
```