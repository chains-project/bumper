```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) throws IOException {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // ...
    }
}
```