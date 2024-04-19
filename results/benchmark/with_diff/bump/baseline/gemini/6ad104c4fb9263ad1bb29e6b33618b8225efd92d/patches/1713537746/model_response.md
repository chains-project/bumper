```java
import org.bouncycastle.crypto.tls.AlertLevel;
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;

public class ChachaDecoder {

    public void decode(byte[] buf, int off, int len) throws IOException {
        if (len < 1) {
            throw new TlsFatalAlert(AlertLevel.fatal, AlertDescription.decode_error);
        }

        int alertLevel = buf[off] & 0xff;
        int alertDescription = buf[off + 1] & 0xff;

        if (alertLevel != AlertLevel.fatal && alertLevel != AlertLevel.warning) {
            throw new TlsFatalAlert(AlertLevel.fatal, AlertDescription.decode_error);
        }

        if (alertDescription < AlertDescription.close_notify || alertDescription > AlertDescription.user_canceled) {
            throw new TlsFatalAlert(AlertLevel.fatal, AlertDescription.decode_error);
        }

        // TODO: Handle the alert
    }
}
```