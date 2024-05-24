```java
import org.bouncycastle.crypto.tls.AlertLevel;

import java.io.IOException;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) throws IOException {
        if (len < 12) {
            throw new TlsFatalAlert(AlertLevel.fatal, AlertDescription.decode_error);
        }
    }
}
```