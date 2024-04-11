Here is a fixed version of the failing method in `ChachaDecoder.java`:

```java
import java.io.IOException;
import java.util.logging.Logger;

import org.bouncycastle.crypto.StreamCipher;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.crypto.params.ParametersWithIV;

public class ChachaDecoder {
    // existing code

    private void decodeRecord(InputStream in, OutputStream out) throws IOException {
        // existing code

        try {
            if (type != TlsUtils.ApplicationData) {
                throw new TlsFatalAlert(AlertDescription.unexpected_message);
            }

            // existing code
        } catch (RuntimeException e) {
            logger.log(Level.FINE, "decodeRecord: " + e.toString(), e);
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }
    }
}
```

Note that I replaced the usage of `TlsFatalAlert` constructor and `getAlertDescription` method with their respective new added methods `TlsFatalAlert(AlertDescription)` and `AlertDescription.unexpected_message`/`AlertDescription.decode_error`.