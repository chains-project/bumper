```java
import org.bouncycastle.crypto.tls.AlertLevel;

public class ChachaDecoder {

    public void decode(byte[] in, int pos, int len) {
        // Check if the alert level is fatal
        if (in[pos] == AlertLevel.fatal) {
            // Get the alert description
            short alertDescription = (short) ((in[pos + 1] & 0xff) | (in[pos + 2] << 8));

            // Throw a TlsFatalAlert exception with the alert description
            throw new TlsFatalAlert(alertDescription);
        }
    }
}
```