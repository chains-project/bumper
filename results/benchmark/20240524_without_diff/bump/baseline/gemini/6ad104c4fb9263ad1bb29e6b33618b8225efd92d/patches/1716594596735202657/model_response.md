```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int nonce = in[inOff] & 0xFF;
        int counter = in[inOff + 1] & 0xFF;
        int key = in[inOff + 2] & 0xFF;
        int stream = in[inOff + 3] & 0xFF;

        // ...
    }
}
```