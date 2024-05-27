```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder {

    public byte[] decode(byte[] in, int inOff, int len) throws IOException {
        if (len < 12) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] nonce = new byte[12];
        System.arraycopy(in, inOff, nonce, 0, 12);

        byte[] key = new byte[32];
        System.arraycopy(in, inOff + 12, key, 0, 32);

        byte[] plaintext = new byte[len - 44];
        System.arraycopy(in, inOff + 44, plaintext, 0, len - 44);

        // TODO: implement ChaCha20 decryption

        return plaintext;
    }
}
```