```java
import org.bouncycastle.crypto.tls.AlertLevel;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] data, int offset, int len) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertLevel.fatal, AlertDescription.decode_error);
        }
    }
}
```