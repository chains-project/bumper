```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] data, int offset, int len) {
        // ...
        if (data[offset] != AlertDescription.fatal) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }
        // ...
    }
}
```