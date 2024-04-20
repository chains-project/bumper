Here's the patched method using the added library method `++`:

```java
import org.bouncycastle.crypto.tls.TlsAlert;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder {

    // ...

    private void decodeRecord(InputStream input) throws IOException {
        // ...

        try {
            // ...

            if (type == Type.alert) {
                int alertDescription = decoder.readUint8();

                // Use the new method to get the AlertDescription
                AlertDescription description = TlsFatalAlert.getAlertDescription(alertDescription);

                throw new TlsFatalAlert(description);
            }

            // ...
        } catch (TlsFatalAlert ex) {
            // ...
        }
    }

    // ...
}
```

This patch replaces the removed method `TlsFatalAlert.getAlertDescription()` with the new method `TlsFatalAlert.getAlertDescription(alertDescription)` to fix the error.