Here is a fixed version of the failing method in ChachaDecoder.java:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import java.io.IOException;

public class ChachaDecoder {
    // existing code

    private void decode(InputStream input, byte[] output) throws IOException {
        // existing code

        try {
            // existing code
        } catch (TlsFatalAlert ex) {
            throw new IOException("Decryption error", ex);
        }
    }

    // existing code
}
```

Note that I imported the new fully qualified name for `TlsFatalAlert` and removed the unused `AlertDescription` import. The `TlsFatalAlert` constructor and `getAlertDescription` method were removed in the new library version, so I removed the corresponding code in the `catch` block. Instead, the exception is now rethrown as an `IOException`.