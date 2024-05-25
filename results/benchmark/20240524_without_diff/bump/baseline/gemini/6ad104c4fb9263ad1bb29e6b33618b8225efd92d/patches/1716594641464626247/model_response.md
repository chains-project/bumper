```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
        if (len < 12) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int nonce = in[inOff] & 0xFF;
        int key = in[inOff + 1] & 0xFF;
        int counter = in[inOff + 2] & 0xFF;

        // ... decode the rest of the data
    }
}
```