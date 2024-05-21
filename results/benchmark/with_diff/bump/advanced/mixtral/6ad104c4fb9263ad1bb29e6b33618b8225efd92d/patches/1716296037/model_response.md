Here's the patched version of the failing method in `ChachaDecoder.java`:

```java
import java.io.IOException;
import java.util.Arrays;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

public class ChachaDecoder {
    // ...

    private void decode(InputStream in, byte[] output, int offset, int length) throws IOException {
        // ...

        if (nonce.length != 12) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }

        // ...
    }

    // ...
}
```

I replaced the removed `TlsFatalAlert` constructor and `getAlertDescription()` method with their respective alternatives:

- `TlsFatalAlert(short)` is replaced with `TlsFatalAlert(AlertDescription)`
- `TlsFatalAlert.getAlertDescription()` is replaced with the constant `AlertDescription.internal_error`