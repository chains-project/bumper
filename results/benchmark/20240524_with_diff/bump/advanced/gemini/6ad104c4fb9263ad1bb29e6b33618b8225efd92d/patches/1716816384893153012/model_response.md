```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // ... rest of the code ...
    }
}
```