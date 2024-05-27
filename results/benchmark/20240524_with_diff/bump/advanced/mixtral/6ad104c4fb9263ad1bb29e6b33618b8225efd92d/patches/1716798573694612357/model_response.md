Here's the patched version of the failing method in `ChachaDecoder.java`:

```java
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

public class ChachaDecoder {
    // ...

    private void decodeHandshakeMessage(byte[] input, int length) throws IOException {
        // ...

        try {
            switch (type) {
                case 20:
                    if (length < 64) {
                        throw new TlsFatalAlert(AlertDescription.decode(AlertDescription.illegal_parameter));
                    }
                    // ...
                // ...
            }
        } catch (TlsFatalAlert ex) {
            logger.log(Level.FINE, "decryption failed: {0}", ex.getMessage());
            throw new TlsFatalAlert(ex.getAlertDescription());
        }
    }

    // ...
}
```

In this patch, I replaced the removed constructor `TlsFatalAlert(short)` with the new method `TlsFatalAlert(TlsFatalAlert.AlertDescription)` and introduced a new variable `ex.getAlertDescription()` to get the `AlertDescription` from the caught `TlsFatalAlert` exception.