```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;
import java.io.InputStream;

public class ChachaDecoder {

    public void decode(InputStream input) throws IOException {
        int alertDescription = input.read();
        if (alertDescription < 0) {
            throw new IOException("End of stream");
        }
        if (alertDescription >= 80) {
            throw new TlsFatalAlert((short) alertDescription);
        }
        throw new IOException("Unexpected alert description: " + alertDescription);
    }
}
```