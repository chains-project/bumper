Here is a fixed version of the failing method in `ChachaDecoder.java`:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import java.io.IOException;

public class ChachaDecoder {
    // existing code

    private void decode(byte[] input, int length) throws IOException {
        // existing code

        if (version == TlsConstants.VERSION_13) {
            if (type == TlsUtilities.Chacha20Poly1305) {
                if (input[2] == 1) {
                    throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
                }
            }
        }

        // existing code
    }
}
```

Note that I had to import the `TlsFatalAlert` class from the new location, and update the import statement for `AlertDescription` to remove it since it is no longer needed. Additionally, I changed the exception being thrown to use the new constructor for `TlsFatalAlert` that takes a `short` argument.